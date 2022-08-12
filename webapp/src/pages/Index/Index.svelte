<script>
    import ProfileEditor from "./page-components/ProfileEditor.svelte";
    import radagon_icon from "../../icons/Degradado4.svg";
    import law_of_regression from "../../icons/Degradado9.svg";
    import CustomerBoughtCourses from './page-components/CoursesContainer.svelte';
    
    window.scrollTo(0, 0);
    
</script>


<main id="cordelia-courses-page">
    <div id="radagon-icon" class="erdtree">
        {@html radagon_icon}
    </div>
    <div id="law-of-regression" class="erdtree">
        {@html law_of_regression}
    </div>
    <div id="ccp-page-content">
        <ProfileEditor/>
        <div class="ccp-spacer">
            <CustomerBoughtCourses/>
        </div>
    </div>
</main>


<style>
    #cordelia-courses-page {
        --ccp-page-height: 285.93vh;

        width: 100%;
        position: relative;
        height: var(--ccp-page-height);
        overflow-x: hidden;
        max-width: 100%;
        background-color: var(--theme-three-color);
        padding: calc(calc(var(--spacing-h1) * .5) + var(--spacing-h1)) 0 0 calc(var(--spacing-h1) * 2.3);
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
            width: 60rem;
            top: 70%;
            left: 70%;
            filter: blur(30px);
}
    
    /*=====  End of Golden Order  ======*/
    

    #ccp-page-content {
        width: 52%;
    }

    .ccp-spacer {
        margin-top: var(--spacing-h1);
    }
    
</style>