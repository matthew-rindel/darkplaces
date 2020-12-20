cmake_minimum_required(VERSION 3.16)
project(darkplaces)

find_package(SDL2 REQUIRED)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_compile_definitions(CONFIG_MENU)
option(DP_VIDEO_CAPTURE "Whether or not the game should be compiled with video capture support." OFF)

add_library(darkplaces-build-info STATIC builddate.c)
add_library(darkplaces-core-sdl STATIC sys_sdl.c vid_sdl.c thread_sdl.c)
add_library(darkplaces-common STATIC
        bih.c
        crypto.c
        cd_shared.c
        cl_cmd.c
        cl_collision.c
        cl_demo.c
        cl_ents.c
        cl_ents4.c
        cl_ents5.c
        cl_ents_nq.c
        cl_ents_qw.c
        cl_input.c
        cl_main.c
        cl_parse.c
        cl_particles.c
        cl_screen.c
        cl_video.c
        cl_video_libavw.c
        clvm_cmds.c
        cmd.c
        collision.c
        com_crc16.c
        com_ents.c
        com_ents4.c
        com_game.c
        com_list.c
        com_msg.c
        common.c
        console.c
        csprogs.c
        curves.c
        cvar.c
        dpvsimpledecode.c
        filematch.c
        fractalnoise.c
        fs.c
        ft2.c
        utf8lib.c
        gl_backend.c
        gl_draw.c
        gl_rmain.c
        gl_rsurf.c
        gl_textures.c
        hmac.c
        host.c
        image.c
        image_png.c
        jpeg.c
        keys.c
        lhnet.c
        libcurl.c
        mathlib.c
        matrixlib.c
        mdfour.c
        meshqueue.c
        mod_skeletal_animatevertices_sse.c
        mod_skeletal_animatevertices_generic.c
        model_alias.c
        model_brush.c
        model_shared.c
        model_sprite.c
        netconn.c
        palette.c
        polygon.c
        portals.c
        protocol.c
        prvm_cmds.c
        prvm_edict.c
        prvm_exec.c
        r_explosion.c
        r_lightning.c
        r_modules.c
        r_shadow.c
        r_sky.c
        r_sprites.c
        r_stats.c
        sbar.c
        sv_ccmds.c
        sv_demo.c
        sv_ents.c
        sv_ents4.c
        sv_ents5.c
        sv_ents_csqc.c
        sv_ents_nq.c
        sv_main.c
        sv_move.c
        sv_phys.c
        sv_save.c
        sv_send.c
        sv_user.c
        svbsp.c
        svvm_cmds.c
        sys_shared.c
        taskqueue.c
        vid_shared.c
        view.c
        wad.c
        world.c
        zone.c)

add_library(darkplaces-sound STATIC
        snd_main.c snd_mem.c snd_mix.c snd_ogg.c snd_wav.c)

if(SND_BACKEND STREQUAL "sdl")
    target_sources(darkplaces-sound PRIVATE snd_sdl.c)
elseif(SND_BACKEND STREQUAL "oss")
    target_sources(darkplaces-sound PRIVATE snd_oss.c)
endif()

if (DP_VIDEO_CAPTURE)
    target_sources(darkplaces-common PRIVATE
                    cap_avi.c cap_ogg.c)
endif()

add_library(darkplaces-menu STATIC
        menu.c mvm_cmds.c)

add_executable(darkplaces-server sys_unix.c vid_null.c thread_null.c snd_null.c)
target_link_libraries(darkplaces-server darkplaces-build-info darkplaces-menu darkplaces-common)

if (SDL2_FOUND)
    include_directories(${SDL2_INCLUDE_DIRS})
    add_executable(darkplaces sys_sdl.c)
    target_link_libraries(darkplaces darkplaces-build-info darkplaces-core-sdl darkplaces-menu darkplaces-sound darkplaces-common ${SDL2_LIBRARIES})
endif()

if(MSVC)
    target_compile_options(darkplaces PRIVATE $<$<CONFIG:RELEASE>:/O2>)
    target_compile_options(darkplaces-core-sdl PRIVATE $<$<CONFIG:RELEASE>:/O2>)
    target_compile_options(darkplaces-menu PRIVATE $<$<CONFIG:RELEASE>:/O2>)
    target_compile_options(darkplaces-sound PRIVATE $<$<CONFIG:RELEASE>:/O2>)
    target_compile_options(darkplaces-common PRIVATE $<$<CONFIG:RELEASE>:/O2>)
else()
    target_compile_options(darkplaces PRIVATE $<$<CONFIG:RELEASE>:-O3>)
    target_compile_options(darkplaces-core-sdl PRIVATE $<$<CONFIG:RELEASE>:-O3>)
    target_compile_options(darkplaces-menu PRIVATE $<$<CONFIG:RELEASE>:-O3>)
    target_compile_options(darkplaces-sound PRIVATE $<$<CONFIG:RELEASE>:-O3>)
    target_compile_options(darkplaces-common PRIVATE $<$<CONFIG:RELEASE>:-O3>)
endif()