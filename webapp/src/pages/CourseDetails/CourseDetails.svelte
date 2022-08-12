<script>
    import radagon_icon from "../../icons/Degradado4.svg";
    import law_of_regression from "../../icons/Degradado9.svg";
    import SideBar from "./page-components/SideBar.svelte";

    window.scrollTo(0, 0);

    export let params = {};
    const { course_id } = params;
</script>

<main id="course-details-page">
    <div id="radagon-icon" class="erdtree">
        {@html radagon_icon}
    </div>
    <div id="law-of-regression" class="erdtree">
        {@html law_of_regression}
    </div>
    <div id="cdp-page-content">
        <div id="cdp-pc-course-header"></div>
        <div id="cdp-pc-course-panel">
            <div id="cdp-cp-video-wrapper">
                <div id="cdp-cp-vw-media">
                    <img src="/resources/Fotografias/Corde-102-original.webp" alt="">
                </div>
            </div>
            <div id="cdp-cp-sidepanel">
                <SideBar/>
            </div>
            <div id="cdp-cp-tabs">
                <div class="cdp-cp-tab">Descripcion</div>
                <div class="cdp-cp-tab">Opiniones</div>
                <div class="cdp-cp-tab">Recursos</div>
            </div>
            <div id="cdp-cp-controls">
                <div id="cdp-cp-desc-control">
                    <h3 class="cdp-cp-dc-title">Lorem ipsum dolor sit amet</h3>
                    <p class="cdp-cp-dc-desc">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
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
        overflow-x: hidden;
        width: 100%;
        max-width: 100%;
        display: flex;
        min-height: var(--ccp-page-height);
        background-color: var(--theme-three-color);
        justify-content: center;
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
            top: 40%;
            left: 70%;
            filter: blur(30px);
        }
    
    /*=====  End of Golden Order  ======*/
    
    #cdp-page-content {
        width: 100%;
    }
    
    #cdp-pc-course-panel {
        display: grid;
        height: 100vh;
        width: 100%;
        grid-template: repeat(8, 1fr) / repeat(6, 1fr);
        grid-template-areas: 
            'video-player video-player video-player video-player course-sidebar course-sidebar'
            'video-player video-player video-player video-player course-sidebar course-sidebar'
            'video-player video-player video-player video-player course-sidebar course-sidebar'
            'video-player video-player video-player video-player course-sidebar course-sidebar'
            'course-controls-tabs course-controls-tabs course-controls-tabs course-controls-tabs course-sidebar course-sidebar'
            'course-controls course-controls course-controls course-controls course-sidebar course-sidebar'
            'course-controls course-controls course-controls course-controls course-sidebar course-sidebar'
            'course-controls course-controls course-controls course-controls course-sidebar course-sidebar';
        }
        
    /* #cdp-pc-course-panel * {
            border: 1px solid red;
    } */
    

    /* Video Wrapper */

    #cdp-cp-video-wrapper {
        grid-area: video-player;
    }

    #cdp-cp-vw-media {
        box-sizing: border-box;
        width: 100%;
        height: 100%;
        background: var(--theme-color);
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
        grid-area: course-sidebar;
        z-index: 3;
    }
    
    /* Tabs */

    #cdp-cp-tabs {
        display: flex;
        box-sizing: border-box;
        grid-area: course-controls-tabs;
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

    @media (pointer: fine) {
        .cdp-cp-tab:hover {
            color: var(--theme-color);
        }
    }

    /* Controls */

    #cdp-cp-controls {
        grid-area: course-controls;
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

</style>