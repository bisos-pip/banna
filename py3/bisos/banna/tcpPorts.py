# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= TCP PortNu Registrar of BANNA (Bisos Assigned Names and Numbers Authority)
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/PyFwrk/bisos-pip/bisos.cs/_nodeBase_/fullUsagePanel-en.org][BISOS CmndSvcs Panel]]   [[elisp:(org-cycle)][| ]]
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
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
** This File: /bisos/git/bxRepos/bisos-pip/siteRegistrars/py3/bisos/siteRegistrars/csSiteRegBox.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= " :title "*Py Library IMPORTS*" :comment "-- with classification based framework/imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- with classification based framework/imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from dataclasses import dataclass, field


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Data Classes " :anchor ""  :extraInfo "Data Class Definitions"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Data Classes _: |]]  Data Class Definitions  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:class/decl :className "TcpPortNuInfo" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of a  Interface"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /TcpPortNuInfo/  superClass=object =Abstraction of a  Interface=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class TcpPortNuInfo(object):
####+END:
    """
** Abstraction of
** hereIp is the 127.0.22.x address of <hereName>.here in /etc/hosts (see bannaForEtcHosts).
   Like portNu, it is assigned once and never recomputed: a new entry never moves an
   existing one. None means the port has no .here name.
** hereName defaults to portName. It differs when the name humans browse belongs to
   another port of the same service (kafka.here is served by the kafbatUi port).
"""
    portNu: int | None = None
    portName: str | None = None
    portDescription: str | None = None
    assignedBy: str | None = None
    assignmentDate:  str | None = None
    hereIp: str | None = None
    hereName: str | None = None


####+BEGIN: b:py3:class/decl :className "TcpPortsAssignedList" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of a  Interface"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /TcpPortsAssignedList/  superClass=object =Abstraction of a  Interface=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class TcpPortsAssignedList(object):
####+END:
    """
** Abstraction of
"""
    tcpPortsList: dict [str, TcpPortNuInfo] = field(default_factory=dict)

    # Singleton using New
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Singleton Instantiation
tcpPortsAssignedList = TcpPortsAssignedList()


csPlayerPerf = TcpPortNuInfo(
    portNu=23001,
    portName='csPlayerPerf',
    portDescription="Backend API performer service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.103",
)
tcpPortsAssignedList.tcpPortsList[csPlayerPerf.portName or 'csPlayerPerf'] = csPlayerPerf

csPlayerUi = TcpPortNuInfo(
    portNu=24001,
    portName='csPlayerUi',
    portDescription="Reveal Gatsby site wrapping csLineInvoker and others",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.105",
)
tcpPortsAssignedList.tcpPortsList[csPlayerUi.portName or 'csPlayerUi'] = csPlayerUi

csLineInvoker = TcpPortNuInfo(
    portNu=24002,
    portName='csLineInvoker',
    portDescription="Line invoker service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.101",
)
tcpPortsAssignedList.tcpPortsList[csLineInvoker.portName or 'csLineInvoker'] = csLineInvoker

sonCliPlayerUi = TcpPortNuInfo(
    portNu=24003,
    portName='sonCliPlayerUi',
    portDescription="SON CLI player UI service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.109",
)
tcpPortsAssignedList.tcpPortsList[sonCliPlayerUi.portName or 'sonCliPlayerUi'] = sonCliPlayerUi

sonCliLineInvoker = TcpPortNuInfo(
    portNu=24004,
    portName='sonCliLineInvoker',
    portDescription="SON CLI line invoker service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.107",
)
tcpPortsAssignedList.tcpPortsList[sonCliLineInvoker.portName or 'sonCliLineInvoker'] = sonCliLineInvoker

starterSidebar = TcpPortNuInfo(
    portNu=24005,
    portName='starterSidebar',
    portDescription="Starter sidebar service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.111",
)
tcpPortsAssignedList.tcpPortsList[starterSidebar.portName or 'starterSidebar'] = starterSidebar

airflow = TcpPortNuInfo(
    portNu=24006,
    portName='airflow',
    portDescription="airflow (ver 3.2.2)",
    assignedBy="Mohsen",
    assignmentDate="<2026-06-27 Fri 16:44>",
    hereIp="127.0.22.100",
)
tcpPortsAssignedList.tcpPortsList[airflow.portName or 'airflow'] = airflow

kafka = TcpPortNuInfo(
    portNu=24007,
    portName='kafka',
    portDescription="kafka broker, PLAINTEXT client listener (ver 4.3.1)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-09 Fri 21:30>",
)
tcpPortsAssignedList.tcpPortsList[kafka.portName or 'kafka'] = kafka

kafkaController = TcpPortNuInfo(
    portNu=24008,
    portName='kafkaController',
    portDescription="kafka KRaft controller listener (ver 4.3.1)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-09 Fri 21:30>",
)
tcpPortsAssignedList.tcpPortsList[kafkaController.portName or 'kafkaController'] = kafkaController

kafbatUi = TcpPortNuInfo(
    portNu=24009,
    portName='kafbatUi',
    portDescription="kafbat UI, web UI for kafka (ver 1.5.0)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-09 Fri 21:30>",
    hereName="kafka",
    hereIp="127.0.22.113",
)
tcpPortsAssignedList.tcpPortsList[kafbatUi.portName or 'kafbatUi'] = kafbatUi

prometheus = TcpPortNuInfo(
    portNu=24010,
    portName='prometheus',
    portDescription="prometheus server, web UI and HTTP API (ver 3.15.0)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-15 Thu 23:00>",
    hereIp="127.0.22.114",
)
tcpPortsAssignedList.tcpPortsList[prometheus.portName or 'prometheus'] = prometheus

grafana = TcpPortNuInfo(
    portNu=24011,
    portName='grafana',
    portDescription="grafana server, web UI and HTTP API (ver 13.2.4)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-15 Thu 23:00>",
    hereIp="127.0.22.115",
)
tcpPortsAssignedList.tcpPortsList[grafana.portName or 'grafana'] = grafana

prometheusNodeExporter = TcpPortNuInfo(
    portNu=24012,
    portName='prometheusNodeExporter',
    portDescription="prometheus node_exporter, host metrics scraped by prometheus (ver 1.12.1)",
    assignedBy="Mohsen",
    assignmentDate="<2026-10-15 Thu 23:00>",
)
tcpPortsAssignedList.tcpPortsList[prometheusNodeExporter.portName or 'prometheusNodeExporter'] = prometheusNodeExporter



csPlayerPerf_dev = TcpPortNuInfo(
    portNu=23501,
    portName='csPlayerPerf_dev',
    portDescription="Backend API performer service (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.104",
)
tcpPortsAssignedList.tcpPortsList[csPlayerPerf_dev.portName or 'csPlayerPerf_dev'] = csPlayerPerf_dev

csPlayerUi_dev = TcpPortNuInfo(
    portNu=25001,
    portName='csPlayerUi_dev',
    portDescription="Reveal Gatsby site wrapping csLineInvoker and others (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.106",
)
tcpPortsAssignedList.tcpPortsList[csPlayerUi_dev.portName or 'csPlayerUi_dev'] = csPlayerUi_dev

csLineInvoker_dev = TcpPortNuInfo(
    portNu=25002,
    portName='csLineInvoker_dev',
    portDescription="Line invoker service (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.102",
)
tcpPortsAssignedList.tcpPortsList[csLineInvoker_dev.portName or 'csLineInvoker_dev'] = csLineInvoker_dev

sonCliPlayerUi_dev = TcpPortNuInfo(
    portNu=25003,
    portName='sonCliPlayerUi_dev',
    portDescription="SON CLI player UI service (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.110",
)
tcpPortsAssignedList.tcpPortsList[sonCliPlayerUi_dev.portName or 'sonCliPlayerUi_dev'] = sonCliPlayerUi_dev

sonCliLineInvoker_dev = TcpPortNuInfo(
    portNu=25004,
    portName='sonCliLineInvoker_dev',
    portDescription="SON CLI line invoker service (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.108",
)
tcpPortsAssignedList.tcpPortsList[sonCliLineInvoker_dev.portName or 'sonCliLineInvoker_dev'] = sonCliLineInvoker_dev

starterSidebar_dev = TcpPortNuInfo(
    portNu=25005,
    portName='starterSidebar_dev',
    portDescription="Starter sidebar service (development)",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
    hereIp="127.0.22.112",
)
tcpPortsAssignedList.tcpPortsList[starterSidebar_dev.portName or 'starterSidebar_dev'] = starterSidebar_dev


def hereEntries() -> list[tuple[str, str, int | None]]:
    """(hereIp, hereName, portNu) of every port that has a .here name, sorted by hereName.

    The source of the banna dblock of /etc/hosts (bannaInfo.cs -i bannaForEtcHosts).
    """
    entries = [
        (info.hereIp, info.hereName or portName, info.portNu)
        for portName, info in tcpPortsAssignedList.tcpPortsList.items()
        if info.hereIp is not None
    ]
    return sorted(entries, key=lambda entry: entry[1])


def hereIpOf(hereName: str) -> str | None:
    """The 127.0.22.x address of <hereName>.here --- without /etc/hosts having to be current."""
    for hereIp, name, _ in hereEntries():
        if name == hereName:
            return hereIp
    return None


def _hereEntriesValidate() -> None:
    """Two .here names on one IP would silently route to the wrong vhost: refuse at import."""
    seenIps: dict[str, str] = {}
    seenNames: set[str] = set()
    for hereIp, hereName, _ in hereEntries():
        if not hereIp.startswith("127.0.22.") or not 0 <= int(hereIp.rsplit(".", 1)[1]) <= 255:
            raise ValueError(f"banna: {hereName}.here hereIp={hereIp} is outside 127.0.22.0/24")
        if hereIp in seenIps:
            raise ValueError(f"banna: {hereName}.here and {seenIps[hereIp]}.here both have hereIp={hereIp}")
        if hereName in seenNames:
            raise ValueError(f"banna: hereName {hereName} is assigned to more than one port")
        seenIps[hereIp] = hereName
        seenNames.add(hereName)


_hereEntriesValidate()



####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
