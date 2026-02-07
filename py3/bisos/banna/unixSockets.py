# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: =CS-Lib= SocketNu Registrar of BANNA (Bisos Assigned Names and Numbers Authority)
#+end_org """

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: Unix Sockets Registry for BISOS Services
** Registers Unix socket endpoints for local inter-process communication
** Status: In use with BISOS
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
** This File: /bisos/git/bxRepos/bisos-pip/banna/py3/bisos/banna/unixSockets.py
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

from dataclasses import dataclass, field

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Data Classes " :anchor ""  :extraInfo "Data Class Definitions"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Data Classes _: |]]  Data Class Definitions  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:class/decl :className "UnixSocketNuInfo" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of a Unix Socket Interface"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /UnixSocketNuInfo/  superClass=object =Abstraction of a Unix Socket Interface=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class UnixSocketNuInfo(object):
####+END:
    """
** Abstraction of Unix Socket Information
"""
    socketNu: int | None = None
    socketName: str | None = None
    socketDescription: str | None = None
    assignedBy: str | None = None
    assignmentDate: str | None = None


####+BEGIN: b:py3:class/decl :className "UnixSocketsAssignedList" :superClass "object" :classType "basic" :deco "@dataclass" :comment "Abstraction of a Unix Sockets List"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /UnixSocketsAssignedList/  superClass=object =Abstraction of a Unix Sockets List=  [[elisp:(org-cycle)][| ]]
#+end_org """
@dataclass
class UnixSocketsAssignedList(object):
####+END:
    """
** Abstraction of Unix Sockets List
"""
    unixSocketsList: dict [str, UnixSocketNuInfo] = field(default_factory=dict)

    # Singleton using New
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Singleton Instantiation
unixSocketsAssignedList = UnixSocketsAssignedList()


# RPyC Registrars - Using Unix Sockets
svcSiteRegBox = UnixSocketNuInfo(
    socketNu=22222001,
    socketName='svcSiteRegBox',
    socketDescription="RPyC Registry - Site Registration Box",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
)
unixSocketsAssignedList.unixSocketsList[svcSiteRegBox.socketName or 'svcSiteRegBox'] = svcSiteRegBox

svcSiteRegContainer = UnixSocketNuInfo(
    socketNu=22222002,
    socketName='svcSiteRegContainer',
    socketDescription="RPyC Registry - Site Registration Container",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
)
unixSocketsAssignedList.unixSocketsList[svcSiteRegContainer.socketName or 'svcSiteRegContainer'] = svcSiteRegContainer

svcSiteRegistrars = UnixSocketNuInfo(
    socketNu=22222003,
    socketName='svcSiteRegistrars',
    socketDescription="RPyC Registry - Site Registrars",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
)
unixSocketsAssignedList.unixSocketsList[svcSiteRegistrars.socketName or 'svcSiteRegistrars'] = svcSiteRegistrars

svcFacter = UnixSocketNuInfo(
    socketNu=22222004,
    socketName='svcFacter',
    socketDescription="RPyC Facter - System Information Service",
    assignedBy="Mohsen",
    assignmentDate="<2026-02-06 Fri 16:44>",
)
unixSocketsAssignedList.unixSocketsList[svcFacter.socketName or 'svcFacter'] = svcFacter


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
