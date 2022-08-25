<script>
    import CourseHeader from "./page-components/CourseHeader.svelte";
    import law_of_regression from "../../icons/Degradado9.svg";
    import SideBar from "./page-components/SideBar.svelte";
    import radagon_icon from "../../icons/Degradado4.svg";
    import { GetCourseRequest } from '../../libs/HttpRequests';
    import cordelia_storage from "../../libs/local_storage";
    import { onMount } from 'svelte';
    
    let course_data = {
        classes: [
            {
                description: "cargando...",
                title: "cargando...",
                id: "",
                resource_path: "",
                resource_type: "",
                unlocks_on: "2020-07-10 15:00:00.000"
            }
        ],
        description: "",
        id: 0,
        name: "",
        teacher_name: ""
    };
    let selected_class = 0;
    
    const coureses_panel_tabs = {
        DESCRIPTION: "description",
        OPINIONS: "opinions",
        RESOURCES: "resources"
    };
    let selected_tab = coureses_panel_tabs.DESCRIPTION;

    window.scrollTo(0, 0);

    export let params = {};
    const { course_id } = params;

    onMount(() => {
        const local_course_data = cordelia_storage.getCoursesDateils(course_id);
        
        if (local_course_data !== undefined) {
            course_data = local_course_data;
            return;
        }

        const token = cordelia_storage.Token;
        const request = new GetCourseRequest(token, course_id);
        request.do(data => {
            course_data = data;
            cordelia_storage.setCourseDetails(course_id, data);
        });
    });

    const handleNotification = e => {
        const { message } = e.detail;
        notification_text = message;
    }

    const setTab = tab_name => selected_tab = tab_name;

</script>


<main id="course-details-page">
    <div id="radagon-icon" class="erdtree">
        {@html radagon_icon}
    </div>
    <div id="law-of-regression" class="erdtree">
        {@html law_of_regression}
    </div>
    <div id="cdp-page-content">
        <div id="cdp-pc-course-header">
            <CourseHeader course_data={course_data}/>
        </div>
        <div id="cdp-pc-course-panel">
            <div id="cdp-cp-video-wrapper">
                <div id="cdp-cp-vw-media">
                    <img src="/resources/Fotografias/tendencias_course-L.webp" alt="">
                </div>
            </div>
            <div id="cdp-cp-sidepanel">
                <SideBar {course_data} bind:selected_class={selected_class}/>
            </div>
            <div id="cdp-cp-tabs">
                <div on:click={() => setTab(coureses_panel_tabs.DESCRIPTION)} class="cdp-cp-tab {selected_tab === coureses_panel_tabs.DESCRIPTION ? 'cdp-cp-tab-selected' : ''}">Descripcion</div>
                <div on:click={() => setTab(coureses_panel_tabs.OPINIONS)} class="cdp-cp-tab {selected_tab === coureses_panel_tabs.OPINIONS ? 'cdp-cp-tab-selected' : ''}">Opiniones</div>
                <div on:click={() => setTab(coureses_panel_tabs.RESOURCES)} class="cdp-cp-tab {selected_tab === coureses_panel_tabs.RESOURCES ? 'cdp-cp-tab-selected' : ''}">Ver Archivos</div>
            </div>
            <div id="cdp-cp-controls">
                <div id="cdp-cp-desc-control">
                    <h3 class="cdp-cp-dc-title">{course_data.classes[selected_class].title}</h3>
                    <p class="cdp-cp-dc-desc">
                        {course_data.classes[selected_class].description}
                    </p>
                </div>
            </div>
        </div>
    </div>
</main>

<style>

    /* * {
        border: 1px solid red;
    } */

    #course-details-page {
        --ccp-page-height: calc(100vh - var(--navbar-height));

        box-sizing: border-box;
        position: relative;
        display: flex;
        overflow: hidden;
        width: 100%;
        max-width: 100%;
        flex-direction: column;
        min-height: var(--ccp-page-height);
        background-color: var(--theme-three-color);
        align-items: center;
        padding: calc(var(--spacing-h1) * .5) calc(var(--spacing-h1) * 2.5);
    }

    /*=============================================
    =            Golden Order            =
    =============================================*/
    
        .erdtree {
            position: absolute;
            border-radius: 50%;
            z-index: 1;
        }

        #radagon-icon {
            width: 33rem;
            background: #cbdcf87c 0% 0% no-repeat padding-box;
            filter: blur(50px);
            /* opacity: 0.8; */
            top: 10%;
            left: -6%;
        }

        #law-of-regression {        
            width: 40rem;
            top: 37%;
            left: 70%;
            filter: blur(30px);
        }
    
    /*=====  End of Golden Order  ======*/
    
    #cdp-page-content {
        width: 100%;
    }

    #cdp-pc-course-header {
        position: relative;
        z-index: 2;
    }
    
    #cdp-pc-course-panel {
        display: grid;
        height: 100vh;
        width: 100%;
        grid-template: repeat(8, 1fr) / repeat(6, 1fr);
        grid-template-areas: 
            'vvv vvv vvv vvv sss sss'
            'vvv vvv vvv vvv sss sss'
            'vvv vvv vvv vvv sss sss'
            'vvv vvv vvv vvv sss sss'
            'ttt ttt ttt ttt sss sss'
            'ccc ccc ccc ccc sss sss'
            'ccc ccc ccc ccc sss sss'
            'ccc ccc ccc ccc sss sss';
        }
        
    /* #cdp-pc-course-panel * {
            border: 1px solid red;
    } */
    

    /* Video Wrapper */

    #cdp-cp-video-wrapper {
        grid-area: vvv;
    }

    #cdp-cp-vw-media {
        box-sizing: border-box;
        width: 100%;
        height: 100%;
    }

    #cdp-cp-video-wrapper img {
        object-fit: cover;
        max-height: 100%;
        min-height: 100%;
        max-width: 100%;
        min-width: 100%;
    }

    /* Sidepanel */

    #cdp-cp-sidepanel {
        position: relative;
        background: white;
        grid-area: sss;
        z-index: 3;
    }
    
    /* Tabs */

    #cdp-cp-tabs {
        display: flex;
        box-sizing: border-box;
        grid-area: ttt;
        padding: 0 var(--spacing-h2);
        align-items: center;
    }

    .cdp-cp-tab {
        cursor: default;
        font-size: var(--font-size-2);
        color: var(--dark-light-color);
        margin-right: var(--spacing-h2);
        transition: all .1s ease-in-out;
    }

    .cdp-cp-tab.cdp-cp-tab-selected {
        font-weight: 500;
        color: var(--theme-two-color);
    }

    @media (pointer: fine) {
        .cdp-cp-tab:hover {
            color: var(--theme-color);
        }
    }

    /* Controls */

    #cdp-cp-controls {
        grid-area: ccc;
    }

    .cdp-cp-dc-title {
        font-family: var(--font-texts);
        font-size: var(--font-size-h4);
        color: var(--theme-five-color);
        margin-bottom: var(--spacing-3);
    }

    .cdp-cp-dc-desc {
        width: 90%;
        font-size: var(--font-size-2);
        color: var(--dark-light-color);
    }

    @media only screen and (max-width: 768px) {
        #radagon-icon {
            top: 0%;
            left: -10%;
        }

        #course-details-page {
            --ccp-page-height: 270vh;

            box-sizing: border-box;
            position: relative;
            display: flex;
            width: 100%;
            max-width: 100%;
            height: auto;
            flex-direction: column;
            padding: calc(var(--spacing-h1) * .5) 0;
        }

        #cdp-pc-course-panel {
            position: relative;
            display: grid;
            height: var(--ccp-page-height);
            width: 100%;
            z-index: 2;
            grid-template: repeat(25, 1fr) / repeat(3, 1fr);
            grid-template-areas: 
                'vvv vvv vvv'
                'vvv vvv vvv'
                'vvv vvv vvv'
                'vvv vvv vvv'
                'ttt ttt ttt'
                'ttt ttt ttt'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'ccc ccc ccc'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                'sss sss sss'
                ;
        }

        #cdp-cp-vw-media {
            padding: var(--spacing-2);
        }

        #cdp-cp-video-wrapper img {
            border-radius: var(--boxes-roundness);
        }

        #cdp-cp-tabs {
            display: flex;
            flex-direction: column;
            padding: var(--spacing-2);
            align-items: center;
        }

        .cdp-cp-tab {
            font-size: var(--font-size-1);
            color: var(--dark-light-color);
            margin: var(--spacing-2) 0;
            transition: all .1s ease-in-out;
        }

        #cdp-cp-controls {
            padding: var(--spacing-3);
        }
    }

</style>