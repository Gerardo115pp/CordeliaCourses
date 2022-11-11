<script>
    import { newNotification } from "../../../components/Notifications/events";

    import check_icon from "../../../icons/Check.svg";

    export let course_data = {
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
    export let selected_class = 0;

    const isClassUnlocked = class_data => {
        return class_data.resource_path !== "";
    }



    const getUnlockedPercentage = classes => {
        const unlocked_classes = classes.filter(isClassUnlocked);
        console.log(unlocked_classes.length);
        let percentage = Math.round((unlocked_classes.length / classes.length) * 100);
        const percentage_bar = document.querySelector(".completed-bar-progress");
        if (percentage_bar !== null) {
            window.setTimeout(() => {
                percentage_bar.style.setProperty("--completed-bar-progress-width", `${percentage}%`);
            }, 80);
        }
        return percentage;
    }

    const getClassTitlePrefix = class_num => {
        let prefix = class_num.toString();
        if (class_num < 10) {
            prefix = `0${prefix}`;
        }
        return prefix+". ";
    }

    const selectClass = class_index => {
        const class_data = course_data.classes[class_index];

        if (!isClassUnlocked(class_data)) {
            newNotification('Esta clase aun no está disponible');
            return;
        }

        selected_class = class_index;
    }

</script>

<div id="course-data-sidebar">
    <div id="cds-course-about">
        <h2>sobre este curso</h2>
        <div id="cds-ca-profesor-data-wrapper">
            <div id="cds-ca-pdw-profesor-profile-pic">
                <img src="/resources/Fotografias/profile_cord-L.webp" alt="profesor">
            </div>
            <div id="cds-ca-pwd-name">
                <h3>{course_data.teacher_name}</h3>
                <p>Consultora de Imagen y Moda</p>
            </div>
            <p class="cds-ca-pwd-description">
                {course_data.description}
            </p>
        </div>
    </div>
    <div id="cds-course-lectures">
        <div id="cds-cl-head-panel">
            <h2>temario del curso</h2>
            <div id="cds-cl-hp-progress">
                <span class="completed-percenage">Completado {getUnlockedPercentage(course_data.classes)}%</span>
                <span class="completed-count">{course_data.classes.filter(isClassUnlocked).length}/{course_data.classes.length}</span>
                <div class="completed-bar">
                    <div class="completed-bar-container">
                        <div class="completed-bar-progress"></div>
                    </div>
                </div>
            </div>
        </div>
        <div id="cds-cl-lectures-container">
            {#each course_data.classes as lecture, h}
                <div on:click={() => selectClass(h)} class={`lecture-item ${isClassUnlocked(lecture) ? 'lecture-unlocked' : 'lecture-locked'} ${selected_class === h ? 'selected-lecture' : ''}`}>
                    <span class="lecture-name">{getClassTitlePrefix(h+1)}{lecture.title}</span>
                    <span class="lecture-check icon-wrapper">{@html check_icon}</span>
                </div>
            {/each}
        </div>
    </div>
</div>

<style>
    #course-data-sidebar {
        display: grid;
        grid-template: repeat(3, 1fr) / 1fr;
        padding: var(--spacing-4) 0;
    }

    /* Top header */
    
    #cds-course-about {
        display: flex;
        grid-row: 1 / 2;
        flex-direction: column;
        align-items: center;
        border-bottom: 4px solid var(--theme-four-color);
    }

    #cds-course-about h2 {
        box-sizing: border-box;
        width: 100%;
        text-align: left;
        font-size: var(--font-size-4);
        padding: 0 var(--spacing-4);
    }

    #cds-ca-profesor-data-wrapper {
        width: 80%;
        display: grid;
        grid-template: repeat(2, 1fr) / repeat(3, 1fr);
        margin: var(--spacing-h4) 0;
        gap: var(--spacing-2);
    }

    #cds-ca-pdw-profesor-profile-pic {
        --profesor-image-size: 5vw; 
        grid-column: 1 / 2;
    }
    
    #cds-ca-pdw-profesor-profile-pic img {
        object-fit: cover;
        width: var(--profesor-image-size);
        height: var(--profesor-image-size);
        border-radius: 50%;
    }

    #cds-ca-pwd-name {
        display: flex;
        grid-column: 2 / span 2;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
    }

    #cds-ca-pwd-name h3 {
        font-family: var(--font-texts);
        font-weight: bold;
    }

    #cds-ca-pwd-name p {
        color: var(--dark-light-color);
        margin: .6ex 0;
    }

    .cds-ca-pwd-description {
        width: 90%;
        color: var(--dark-light-color);
        font-size: calc(var(--font-size-1) * 1.25);
        grid-area: 2 / 1 / 3 / 4;
    }

    /* Lectures */

    #cds-course-lectures {
        display: flex;
        flex-direction: column;
        grid-row: 2 / 4;
        align-items: center;
        padding: var(--spacing-3) 0;
    }

    #cds-cl-head-panel {
        display: flex;
        flex-direction: column;
        height: 5vw;
        padding: var(--spacing-4) 0;
        justify-content: space-between;
    }

    #cds-cl-head-panel h2 {
        font-size: var(--font-size-h4);
    } 

    #cds-cl-hp-progress {
        display: grid;
        grid-template: repeat(2, 1fr) / repeat(4, 1fr);
        row-gap: var(--spacing-1);
        color: var(--dark-light-color);
    }

    .completed-percenage {
        grid-area: 1 / 1 / 2 / 4;
        text-align: left; 
    }

    .completed-count {
        grid-area: 1 / 4 / 2 / 5;
        text-align: right;
    }

    .completed-bar {
        grid-area: 2 / 1 / 3 / 5;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .completed-bar-container {
        width: 100%;
        height: 1ex;
        background-color: var(--theme-light-five-color);
    }

    .completed-bar-progress {
        --completed-bar-progress-width: 20%;
        width: var(--completed-bar-progress-width);
        height: 100%;
        background-color: var(--theme-five-color);
    }

    /* Lectures */

    #cds-cl-lectures-container {
        width: 80%;
        max-height: 20vw;
        overflow-y: auto;
    }

    /* #cds-cl-lectures-container::-webkit-scrollbar {
        width: 0;
    } */

    .lecture-item {
        display: flex;
        user-select: none;
        font-size: var(--font-size-2);
        margin: var(--spacing-3) 0;
        justify-content: space-between;
        cursor: pointer;
        color: var(--dark-light-color);
        transition: all .2s ease-in-out;
    }

    .lecture-item.lecture-locked {
        text-decoration: line-through;
    }

    .lecture-item.lecture-unlocked .lecture-check {
        fill: var(--ready);
    }

    .lecture-item.selected-lecture {
        color: var(--theme-five-color);
    }

    @media only screen and (max-width: 768px) {
        
        #cds-ca-profesor-data-wrapper {
            gap: var(--spacing-1);
        }

        #cds-ca-profesor-data-wrapper p {
            margin: .5em 0;
        }

        #cds-ca-pdw-profesor-profile-pic {
            --profesor-image-size: 30vw;
        }

        #cds-ca-pwd-name p {
            font-size: var(--font-size-small);
        }

        #cds-cl-head-panel {
            height: calc(var(--ccp-page-height) * 0.04);
        }
        
        #cds-cl-head-panel h2 {
            font-size: var(--font-size-h3);
        } 

        #cds-cl-lectures-container {
            --lectures-container-height: calc(var(--ccp-page-height) * 0.18);

            max-height: var(--lectures-container-height);
            height: var(--lectures-container-height);
        }
    }

</style>