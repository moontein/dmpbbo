# https://stackoverflow.com/questions/35765106/symbolic-links-cmake
macro(install_symlink_in_bin filename)
    install(CODE "message(\"-- Creating symlink: ${CMAKE_CURRENT_SOURCE_DIR}/${filename} -> ${PROJECT_SOURCE_DIR}/bin/${filename}\")")
    install(CODE "execute_process(COMMAND ${CMAKE_COMMAND} -E create_symlink ${CMAKE_CURRENT_SOURCE_DIR}/${filename} ${PROJECT_SOURCE_DIR}/bin/${filename})")
endmacro(install_symlink)

add_executable(demoExponentialSystem demoExponentialSystem.cpp)
target_link_libraries(demoExponentialSystem dynamicalsystems ${Boost_LIBRARIES})
install(TARGETS demoExponentialSystem DESTINATION bin)


# macro add_demo_with_python_wrapper
add_executable(demoDynamicalSystems demoDynamicalSystems.cpp)
target_link_libraries(demoDynamicalSystems dynamicalsystems ${Boost_LIBRARIES})
add_custom_target(link_target ALL
                  COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_CURRENT_SOURCE_DIR}/demoDynamicalSystemsWrapper.py" "demoDynamicalSystemsWrapper.py")

install(TARGETS demoDynamicalSystems DESTINATION bin)
install_symlink_in_bin("demoDynamicalSystemsWrapper.py")

