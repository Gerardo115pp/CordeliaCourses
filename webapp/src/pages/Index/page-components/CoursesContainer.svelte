<script>
    import { push } from "svelte-spa-router";

    export let courses = [
        {
            id: "000000-000000-000000-000001",
            title: "Curso de Sistemas de Control",
            description: "Curso de Sistemas de Control",
            thumbnail: "/resources/Fotografias/Corde-164-original.webp"
        },
        {
            id: "000000-000000-000000-000002",
            title: "Curso de Arquitectura de Css",
            description: "Curso de Arquitectura de Css, diseño de paginas web",
            thumbnail: "/resources/Fotografias/Corde-182-original.webp"
        },
        {
            id: "000000-000000-000000-000003",
            title: "Curso de Base de Datos",
            description: "Curso de Base de Datos",
            thumbnail: "/resources/Fotografias/Corde-102-original.webp"
        },
        {
            id: "000000-000000-000000-000004",
            title: "Curso de Programacion",
            description: "Curso de Programacion",
            thumbnail: "/resources/Fotografias/Corde-090-original.webp"
        }
    ];
</script>

<div id="cordelia-customer-courses">
    <h3 class="page-title">mis cursos</h3>
    {#each courses as course}
         <div class="course-item-wrapper">
            <div class="course-thumbnail">
                <img src="{course.thumbnail}" alt="{course.title}">
            </div>
            <div on:click={() => push(`/course/${course.id}`)} class="course-title"><h2>{course.title}</h2></div>
            <div class="course-description">{course.description}</div>
         </div>
    {/each}
</div>

<style>
    #cordelia-customer-courses {
        --ccc-grid-gap: var(--spacing-h3);
        
        box-sizing: border-box;
        display: grid;
        background: var(--theme-dark-four-color);
        grid-template-columns: 1fr;
        row-gap: var(--ccc-grid-gap);
        padding: var(--ccc-grid-gap) var(--spacing-2);
    }

    /* #cordelia-customer-courses * {
        border: 1px solid red;
    } */

    .course-item-wrapper {
        display: grid;
        box-sizing: content-box;
        background: white;
        border-radius: var(--boxes-roundness);
        padding: var(--spacing-h3) var(--ccc-grid-gap);
        height: calc(3 * var(--spacing-h3));
        grid-template: repeat(2, 1fr) / repeat(3, 1fr);
        gap: var(--spacing-2) var(--ccc-grid-gap);
    }

    .course-thumbnail {
        grid-area: 1/ 1/ 3/ 2;
    }
    
    .course-thumbnail img {
        width: 100%;
        border-radius: var(--boxes-roundness);
        height: 100%;
        object-fit: cover;
    }

    .course-title {
        display: flex;
        cursor: pointer;
        grid-area: 1/ 2/ 2/ 4;
        font-size: var(--font-size-3);
        align-items: center;
        color: var(--theme-color);
    }
    
    .course-title h2 {
        width: max-content;
        text-transform: capitalize;
        transition: all 0.3s ease-out;
    }
    
    @media (pointer: fine) {
        .course-title h2:hover {
            transform: scale(1.02);
            transform-origin: center;
        }
    }

    .course-description {
        grid-area: 2/ 2/ 3/ 4;
        font-size: var(--font-size-2);
        color: var(--dark-light-color);
    }

    @media only screen and (max-width: 768px) {
        #cordelia-customer-courses {
            --ccc-grid-gap: var(--spacing-4);
            width: 100%;
        }

        .course-item-wrapper {
            display: grid;
            box-sizing: border-box;
            width: 100%;
            background: white;
            border-radius: var(--boxes-roundness);
            padding: var(--spacing-h3) var(--ccc-grid-gap);
            height: auto;
            grid-template: 50vw repeat(2, 20vw) / repeat(1, 1fr);
            gap: var(--spacing-2);
        }

        .course-thumbnail {
            grid-area: 1/ 1/ 2/ 2;
        }

        .course-thumbnail img {
            width: 100%;
            border-radius: var(--boxes-roundness);
            height: 100%;
            object-fit: fill;
        }      

        .course-title {
            display: flex;
            cursor: pointer;
            grid-area: 2/ 1/ 3/ 2;
            font-size: var(--font-size-2);
            align-items: center;
            color: var(--theme-color);
        }

        .course-title h2 {
            max-width: 74vw;
        }

        .course-description {
            grid-area: 3/ 1/ 4/ 2;
            font-size: var(--font-size-2);
            color: var(--dark-light-color);
        }      
    }
</style>