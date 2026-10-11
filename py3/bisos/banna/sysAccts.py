# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= System Accounts (uid/gid) Registrar of BANNA (Bisos Assigned Names and Numbers Authority)
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
The uid and gid of every system account a BISOS capability creates, assigned once
and never recomputed --- as tcpPorts does for ports --- so that the same account has
the same numbers on every BISOS platform. Files moved between hosts (backups,
restores, rsync, cloned VMs, NFS) keep their owner, and logs and monitoring agree.
** Range: 500-999, starting at 500 and growing upward. This sits inside Debian's
   dynamic system range (Debian Policy 9.2.2: 100-999), deliberately without
   reconfiguring /etc/login.defs or /etc/adduser.conf: adduser --system allocates
   upward from 100 and useradd -r downward from 999, so neither is expected to
   reach the 500s-600s. The rare collision is detected, never silently resolved:
   see useraddScript() and bannaInfo.cs -i bannaSysAcctsVerify.
** 0-99 and 60000-64999 belong to Debian (base-passwd); 1000+ are human accounts.
** Accounts created by Debian packages (e.g. postgres) are NOT registered here: their
   packages allocate them dynamically and BISOS does not override that.
** Status: Starting point
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO Migrate existing hosts' accounts to their registered numbers (usermod/groupmod + chown).
*** TODO Optionally generate a sysusers.d file from this registry.
#+end_org """

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/banna/py3/bisos/banna/sysAccts.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

import grp
import pwd
import shlex

from dataclasses import dataclass, field


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Data Classes " :anchor ""  :extraInfo "Data Class Definitions"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Data Classes _: |]]  Data Class Definitions  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:class/decl :className "SysAcctInfo" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of a System Account"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /SysAcctInfo/  superClass=object =Abstraction of a System Account=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class SysAcctInfo(object):
####+END:
    """
** Abstraction of a system account and its primary group.
** groupName defaults to acctName and gid to uid: for a single-account capability one
   name and one number identify both the account and its group.
** A multi-account capability (qmail) shares groups between its accounts: groupName then
   names the shared group, and every account of that group carries the same gid.
** block names the capability a multi-account allocation belongs to (useraddScriptBlock).
** createHome: whether useradd creates homeDir (-m) or the capability's sbom does (-M).
"""
    acctName: str | None = None
    uid: int | None = None
    gid: int | None = None
    groupName: str | None = None
    acctDescription: str | None = None
    homeDir: str | None = None
    shell: str = "/usr/sbin/nologin"
    createHome: bool = False
    block: str | None = None
    assignedBy: str | None = None
    assignmentDate: str | None = None

    def __post_init__(self):
        if self.gid is None:
            self.gid = self.uid
        if self.groupName is None:
            self.groupName = self.acctName


####+BEGIN: b:py3:class/decl :className "SysAcctsAssignedList" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of the System Accounts List"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /SysAcctsAssignedList/  superClass=object =Abstraction of the System Accounts List=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class SysAcctsAssignedList(object):
####+END:
    """
** Abstraction of the System Accounts List
"""
    sysAcctsList: dict [str, SysAcctInfo] = field(default_factory=dict)

    # Singleton using New
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Singleton Instantiation
sysAcctsAssignedList = SysAcctsAssignedList()

# The range BISOS assigns from. Growing upward from 500 keeps clear of useradd -r,
# which allocates downward from 999.
sysAcctsRange = range(500, 1000)

# 500 is the base of the range and is deliberately left unassigned.

airflow = SysAcctInfo(
    acctName='airflow',
    uid=501,
    acctDescription="Apache Airflow (bisos.airflow)",
    homeDir="/home/airflow",
    shell="/bin/bash",
    createHome=True,
    assignedBy="Mohsen",
    assignmentDate="<2026-10-10 Sat 10:00>",
)
sysAcctsAssignedList.sysAcctsList[airflow.acctName or 'airflow'] = airflow

# 502 was briefly qmail's single number (never on any host); it is free again.

kafka = SysAcctInfo(
    acctName='kafka',
    uid=503,
    acctDescription="Apache Kafka and Kafbat UI (bisos.kafka)",
    homeDir="/var/lib/kafka",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-10 Sat 10:00>",
)
sysAcctsAssignedList.sysAcctsList[kafka.acctName or 'kafka'] = kafka

# 504-509: single-account capabilities, next in line.

# 510-519: the qmail block (bisos.qmail). Classic qmail's seven accounts and two groups:
#   group nofiles (511): alias, qmaild, qmaill, qmailp
#   group qmail   (510): qmailq, qmailr, qmails
# uids 510-516 are the accounts; 517-519 are spare within the block.
# uid and gid are separate number spaces: uid 510 (alias) and gid 510 (qmail) do not clash.
_qmailGids = {'qmail': 510, 'nofiles': 511}
for _uid, _acctName, _groupName, _homeDir, _desc in (
        (510, 'alias',  'nofiles', '/var/qmail/alias', "qmail aliases"),
        (511, 'qmaild', 'nofiles', '/var/qmail',       "qmail daemon (smtpd, qmqpd)"),
        (512, 'qmaill', 'nofiles', '/var/qmail',       "qmail logger"),
        (513, 'qmailp', 'nofiles', '/var/qmail',       "qmail password-file user"),
        (514, 'qmailq', 'qmail',   '/var/qmail',       "qmail queue"),
        (515, 'qmailr', 'qmail',   '/var/qmail',       "qmail remote delivery"),
        (516, 'qmails', 'qmail',   '/var/qmail',       "qmail send"),
):
    sysAcctsAssignedList.sysAcctsList[_acctName] = SysAcctInfo(
        acctName=_acctName,
        uid=_uid,
        gid=_qmailGids[_groupName],
        groupName=_groupName,
        acctDescription=f"{_desc} (bisos.qmail)",
        homeDir=_homeDir,
        block='qmail',
        assignedBy="Mohsen",
        assignmentDate="<2026-10-10 Sat 11:00>",
    )


def sysAcctOf(acctName: str) -> SysAcctInfo:
    """The registered account. KeyError if acctName is not registered."""
    return sysAcctsAssignedList.sysAcctsList[acctName]


def _sorted() -> list[SysAcctInfo]:
    return sorted(sysAcctsAssignedList.sysAcctsList.values(), key=lambda acct: acct.uid or 0)


def etcPasswdLines() -> list[str]:
    """/etc/passwd lines of every registered account, by uid."""
    return [
        f"{a.acctName}:x:{a.uid}:{a.gid}:{a.acctDescription or ''}:{a.homeDir or '/nonexistent'}:{a.shell}"
        for a in _sorted()
    ]


def etcGroupLines() -> list[str]:
    """/etc/group lines of every registered primary group, once per group, by gid."""
    groups = {a.groupName: a.gid for a in _sorted()}
    return [f"{name}:x:{gid}:" for name, gid in sorted(groups.items(), key=lambda item: item[1])]


def blockAccts(block: str) -> list[SysAcctInfo]:
    """The accounts of a multi-account block, by uid. KeyError if there are none."""
    accts = [a for a in _sorted() if a.block == block]
    if not accts:
        raise KeyError(block)
    return accts


def useraddScript(acctName: str) -> str:
    """Idempotent bash that creates the account and its group with the registered numbers.

    - Absent: groupadd -r -g / useradd -r -u -g.
    - Present with the registered numbers: no-op.
    - Present with other numbers (a host set up before this registry): a WARNING on
      stderr and no change. Renumbering an existing account also needs a chown of
      its files, so it is a deliberate migration, not something an sbom does.
    - Registered number held by another account or group: ERROR, exit 1. Never
      fall back to some other number --- that is exactly what this registry prevents.
    """
    a = sysAcctOf(acctName)
    q = shlex.quote
    homeOpt = "-m" if a.createHome else "-M"
    return f"""
# banna sysAccts: {a.acctName} uid={a.uid}, group {a.groupName} gid={a.gid}
if getent group {q(a.groupName)} >/dev/null ; then
    liveGid=$(getent group {q(a.groupName)} | cut -d: -f3)
    [ "$liveGid" = "{a.gid}" ] || \\
        echo "banna: WARNING: group {a.groupName} has gid $liveGid, banna assigns {a.gid} -- see bannaInfo.cs -i bannaSysAcctsVerify" >&2
else
    holder=$(getent group {a.gid} | cut -d: -f1)
    if [ -n "$holder" ] ; then
        echo "banna: ERROR: gid {a.gid} (registered for group {a.groupName}) is held by group $holder" >&2
        exit 1
    fi
    sudo groupadd -r -g {a.gid} {q(a.groupName)}
fi
if getent passwd {q(a.acctName)} >/dev/null ; then
    liveUid=$(id -u {q(a.acctName)})
    [ "$liveUid" = "{a.uid}" ] || \\
        echo "banna: WARNING: account {a.acctName} has uid $liveUid, banna assigns {a.uid} -- see bannaInfo.cs -i bannaSysAcctsVerify" >&2
else
    holder=$(getent passwd {a.uid} | cut -d: -f1)
    if [ -n "$holder" ] ; then
        echo "banna: ERROR: uid {a.uid} (registered for {a.acctName}) is held by account $holder" >&2
        exit 1
    fi
    sudo useradd -r -u {a.uid} -g {q(a.groupName)} {homeOpt} -d {q(a.homeDir or '/nonexistent')} \\
        -s {q(a.shell)} -c {q(a.acctDescription or '')} {q(a.acctName)}
fi
"""


def useraddScriptBlock(block: str) -> str:
    """useraddScript() of every account of a multi-account block, in uid order.

    A shared group is created by its first account and found present by the rest.
    """
    return "".join(useraddScript(a.acctName) for a in blockAccts(block))


def liveDrift() -> list[tuple[str, str, str]]:
    """Compare this host's passwd/group databases with the registry. Read-only.

    Returns (acctName, status, detail); status is one of
      ok        -- present with the registered uid and gid
      absent    -- not created on this host (its capability is not installed)
      differs   -- present with other numbers: needs migration
      conflict  -- absent, and its registered uid or gid is held by another account/group
    """
    results = []
    for a in _sorted():
        try:
            pw = pwd.getpwnam(a.acctName)
        except KeyError:
            holders = []
            try:
                holders.append(f"uid {a.uid} held by {pwd.getpwuid(a.uid).pw_name}")
            except KeyError:
                pass
            try:
                holders.append(f"gid {a.gid} held by group {grp.getgrgid(a.gid).gr_name}")
            except KeyError:
                pass
            results.append((a.acctName, "conflict" if holders else "absent", "; ".join(holders)))
            continue
        if pw.pw_uid == a.uid and pw.pw_gid == a.gid:
            results.append((a.acctName, "ok", f"uid={a.uid} gid={a.gid}"))
        else:
            results.append((a.acctName, "differs",
                            f"live uid={pw.pw_uid} gid={pw.pw_gid}, banna uid={a.uid} gid={a.gid}"))
    return results


def _sysAcctsValidate() -> None:
    """Two accounts on one number would share every file they own: refuse at import.

    uids are unique per account. gids are unique per group: accounts sharing a group
    (a block's shared group) must agree on its gid, and no two groups share a gid.
    """
    def inRange(what: str, num: int | None) -> None:
        if num not in sysAcctsRange:
            raise ValueError(f"banna: {what}={num} is outside {sysAcctsRange.start}-{sysAcctsRange.stop - 1}")

    uidOwner: dict[int, str] = {}
    groupGid: dict[str, int] = {}
    gidGroup: dict[int, str] = {}
    for a in sysAcctsAssignedList.sysAcctsList.values():
        inRange(f"{a.acctName} uid", a.uid)
        inRange(f"{a.acctName} gid", a.gid)
        if a.uid in uidOwner:
            raise ValueError(f"banna: {a.acctName} and {uidOwner[a.uid]} both have uid={a.uid}")
        uidOwner[a.uid] = a.acctName
        if a.groupName in groupGid and groupGid[a.groupName] != a.gid:
            raise ValueError(f"banna: group {a.groupName} has gid {groupGid[a.groupName]} and {a.gid}")
        if a.gid in gidGroup and gidGroup[a.gid] != a.groupName:
            raise ValueError(f"banna: groups {a.groupName} and {gidGroup[a.gid]} both have gid={a.gid}")
        groupGid[a.groupName] = a.gid
        gidGroup[a.gid] = a.groupName


_sysAcctsValidate()


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
