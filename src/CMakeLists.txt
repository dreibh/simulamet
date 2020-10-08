#############################################################################
# PROGRAMS
#############################################################################



#############################################################################
# CONFIGURATION FILES
#############################################################################

INSTALL(PROGRAMS system-info.d/20-simulamet DESTINATION ${CMAKE_INSTALL_FULL_SYSCONFDIR}/system-info.d)

INSTALL(PROGRAMS system-maintenance.d/20-simulamet DESTINATION ${CMAKE_INSTALL_FULL_SYSCONFDIR}/system-maintenance.d)



#############################################################################
# SOURCE DIRECTORIES
#############################################################################

ADD_SUBDIRECTORY(background)
ADD_SUBDIRECTORY(grub)
