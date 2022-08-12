<script>
    import check_icon from "../../../icons/Check.svg";

    export let course_lectures = [
        {
            name: "01. Titulo de la leccion",
            completed: true
        },
        {
            name: "02. Titulo de la leccion",
            completed: true
        },
        {
            name: "03. Titulo de la leccion",
            completed: false
        },
        {
            name: "04. Titulo de la leccion",
            completed: false
        },
        {
            name: "05. Titulo de la leccion",
            completed: false
        },
        {
            name: "06. Titulo de la leccion",
            completed: false
        },
        {
            name: "07. Titulo de la leccion",
            completed: false
        },
        {
            name: "08. Titulo de la leccion",
            completed: false
        },
        {
            name: "09. Titulo de la leccion",
            completed: false
        },
        {
            name: "10. Titulo de la leccion",
            completed: false
        }

    ]
</script>

<div id="course-data-sidebar">
    <div id="cds-course-about">
        <h2>sobre este curso</h2>
        <div id="cds-ca-profesor-data-wrapper">
            <div id="cds-ca-pdw-profesor-profile-pic">
                <img src="/resources/Fotografias/Corde-169-S.webp" alt="profesor">
            </div>
            <div id="cds-ca-pwd-name">
                <h3>cordelia ruiz</h3>
                <p>Consultora de Imagen y Moda</p>
            </div>
            <p class="cds-ca-pwd-description">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.
            </p>
        </div>
    </div>
    <div id="cds-course-lectures">
        <div id="cds-cl-head-panel">
            <h2>temario del curso</h2>
            <div id="cds-cl-hp-progress">
                <span class="completed-percenage">Completado 20%</span>
                <span class="completed-count">2/10</span>
                <div class="completed-bar">
                    <div class="completed-bar-container">
                        <div class="completed-bar-progress"></div>
                    </div>
                </div>
            </div>
        </div>
        <div id="cds-cl-lectures-container">
            {#each course_lectures as lecture}
                <div class={`lecture-item ${lecture.completed ? 'lecture-complete' : 'lecture-incomplete'}`}>
                    <span class="lecture-name">{lecture.name}</span>
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
    }

    .cds-ca-pwd-description {
        width: 90%;
        color: var(--dark-light-color);
        font-size: calc(var(--font-size-1) * 1.25);
        text-align: justify;
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
        row-gap: var(--spacing-2);
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
        width: 20%;
        height: 100%;
        background-color: var(--theme-five-color);
    }

    /* Lectures */

    #cds-cl-lectures-container {
        width: 80%;
        max-height: 25vw;
        overflow-y: auto;
    }

    .lecture-item {
        display: flex;
        font-size: var(--font-size-2);
        margin: var(--spacing-3) 0;
        justify-content: space-between;
        cursor: pointer;
        color: var(--dark-light-color);
    }

    .lecture-item.lecture-complete {
        text-decoration: line-through;
    }

    .lecture-item.lecture-complete .lecture-check {
        fill: var(--ready);
    }



</style>