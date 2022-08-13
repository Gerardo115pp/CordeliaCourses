<script>
    import cordelia_icon from '../../../icons/Luna.svg';

    export let course_data = {
        title: 'Serie Tendencias O/I 2022',
        teacher: 'cordelia ruiz'
    }

</script>

<header id="course-deatail-header">
    <div id="cdh-cord-icon">
        {@html cordelia_icon}
    </div>
    <div id="cdh-title"><h4>{course_data.title}</h4></div>
    <div id="course-teacher">POR: {course_data.teacher}</div>
</header>

<style>
    #course-deatail-header {
        box-sizing: content-box;
        width: 100%;
        padding: var(--spacing-3);
    }

    #course-deatail-header * {
        margin: var(--spacing-3) 0;
    }

    #cdh-cord-icon {
        width: var(--spacing-h4);
    }

    #course-deatail-header #cdh-title h4{
        font-size: var(--font-size-h2);
        text-transform: capitalize;
    }

    #course-teacher {
        font-size: var(--font-size-3);
        color: var(--dark-light-color);
        text-transform: uppercase;
    }
</style>