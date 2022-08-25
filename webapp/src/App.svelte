<script>
    import Router from "svelte-spa-router";
    import { routes } from "./routes.js";
    import Navbar from "./components/Navbar.svelte";
    import Footer from "./components/Footer.svelte";
    import NotificationsPopup from "./components/Notifications/NotificationsPopup.svelte";
</script>

<style global>
    :root {
        /* Colors */
        --theme-color: #454C4E;
        --theme-light-color: #A9AEB4;
        --theme-two-color: #1C1C1C;
        --theme-light-two-color: #464C4E;
        --theme-three-color: #FCF9F2;
        --theme-four-color: #EBD8CA;
        --theme-dark-four-color: #EEE3CC5A;
        --theme-five-color: #AD8E79;
        --theme-light-five-color: #e6cdbc;
        --dark-color: black;
        --dark-light-color: #00000080;
        --placeholder-color: #00000025;
        --clear-color: #F3F4F1;
        --theme-gradient: linear-gradient(270deg, #F3F4F1 0%, #E6E2DF 100%);
        --danger: #E87156;
        --ready: #62C77A;
        --trasparent-theme-color: #ccff6c88;
        --dark-tranparent-background: rgba(0, 0, 0, 0.3);
        


        /* Fonts */
        --font-titles: 'ivymode', cursive;
        --font-text: 'commuters-sans', sans-serif;

        --font-size-1: 1.2257405515832482vh;
        --font-size-2: calc(var(--font-size-1) + calc(var(--font-size-1) * 0.55));
        --font-size-3: calc(var(--font-size-1) + calc(var(--font-size-1) * 0.7));
        --font-size-4: calc(var(--font-size-1) + calc(var(--font-size-1) * 1.1));
        --font-size-h1: calc(var(--font-size-1) * 5.5);
        --font-size-h2: calc(var(--font-size-h1) * 0.80);
        --font-size-h3: calc(var(--font-size-h1) * 0.6);
        --font-size-h4: calc(var(--font-size-h1) * 0.4);
        --font-size-small: calc(var(--font-size-1) * 0.8);
        
        font-size: var(--font-size-1);

        
        /* Spacing */
        --spacing-1: 0.6rem;
        --spacing-2: calc(var(--spacing-1) * 2);
        --spacing-3: calc(var(--spacing-1) * 3);
        --spacing-4: calc(var(--spacing-1) * 4);
        --spacing-h1: calc(var(--spacing-4) * 4);
        --spacing-h2: calc(var(--spacing-h1) * 0.75);
        --spacing-h3: calc(var(--spacing-h1) * 0.5);
        --spacing-h4: calc(var(--spacing-h1) * 0.25);

        /* Misc */
        --navbar-height: 22.172949002217294vh; /* Not used yet */
        --footer-height: 56.72vh; /* Not used yet */
        --boxes-roundness: 6px;
        --letter-spacing: 0.39936px;
        --boxes-shadow: 0px 5px 4px 1px rgba(0, 0, 0, 0.1);
        letter-spacing: var(--letter-spacing);
        
        /* buttons */
        --buttons-padding: var(--spacing-2) var(--spacing-h3);
        --buttons-text-transform: capitalize;
        --btn-font-size: var(--font-size-2);
        --button-roundness: var(--boxes-roundness);
        --button-shadow: var(--boxes-shadow);
        --button-font-weight: 500;


     
    }


    
    /*=============================================
    =            Normalize            =
    =============================================*/
    
    
        * {
            box-sizing: border-box;
        }
    
        :global(body) {
            margin: 0;
            padding: 0;
            font-family: var(--font-text);
        }
    
        
        
    /*=====  End of Normalize  ======*/
        
        
        
    
    /*=============================================
    =            Theme styles            =
    =============================================*/
        
        :global(h1, h2, h3, h4, h5, h6) {
            font-family: var(--font-titles);
            font-weight: 400;
            text-transform: uppercase;
            margin: 0;
        }

        :global(a) {
            color: var(--theme-color);
            font-weight: bold;
            text-decoration: none;
            text-transform: uppercase;
        }
    
        :global(.page-container) {
            width: 100%;
            min-height: calc(100vh - var(--navbar-height));
        }


        :global(.page-title) {
            text-transform: uppercase;
            font-size: var(--font-size-h1);
            font-weight: 300;
        }

        :global(.full-btn) {
            font-family: var(--font-text);
            box-sizing: border-box;
            padding: var(--buttons-padding);
            color: var(--clear-color);
            background-color: var(--theme-color);
            border-radius: var(--button-roundness);
            font-weight: var(--button-font-weight);
            font-size: var(--btn-font-size);
            border: none;
            box-shadow: var(--button-shadow);
            transition: all 0.3s ease-in-out;
            text-transform: var(--buttons-text-transform);
        }

        :global(.full-two-btn) {
            font-family: var(--font-text);
            box-sizing: border-box;
            padding: var(--buttons-padding);
            color: var(--clear-color);
            background-color: var(--theme-five-color);
            border-radius: var(--button-roundness);
            font-weight: var(--button-font-weight);
            font-size: var(--btn-font-size);
            border: none;
            box-shadow: var(--button-shadow);
            transition: all 0.3s ease-in-out;
            text-transform: var(--buttons-text-transform);
        }

        :global(.cordelia-ruiz-brand-label) {
            font-family: var(--font-titles);
            font-weight: 500;
            letter-spacing: 0.656vw;
            text-transform: capitalize;
        }

        :global(.clear-btn) {
            cursor: pointer;
            box-sizing: border-box;
            background-color: rgba(255, 255, 255, 0.658);
            color: var(--dark-color);
            border: 1px solid var(--dark-color);
            padding: 0.5em 2em;
            border-radius: 8px;
            font-weight: bold;
            font-size: var(--btn-font-size);
            box-shadow: 0px 5px 4px 1px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease-in;
            text-transform: uppercase;
        }

        :global(.icon-wrapper) {
            display: flex;
            align-items: center;
            justify-content: center;
            width: var(--spacing-2);
            margin: 0;
        }

        @media (pointer: fine) {
            :global(.clear-btn:hover) {
                background-color: var(--theme-color);
                color: var(--dark-color);
                /* border: none; */
            }

            :global(.full-btn:hover) {
                background-color: var(--theme-four-color);
                color: var(--theme-color);
                transform: scale(1.05);
                box-shadow: 0px 5px 8px 3px rgba(0, 0, 0, 0.18);
            }

            :global(.full-two-btn:hover) {
                background-color: var(--theme-light-five-color);
                color: var(--theme-five-color);
                transform: scale(1.05);
                box-shadow: 0px 5px 8px 3px rgba(0, 0, 0, 0.18);
            }
        }

        :global(.round-image) {
            border-radius: var(--boxes-roundness);
            box-shadow: 0px 5px 17px 4px rgb(0 0 0 / 26%);
        }

        :global(.round-box) {
            border-radius: var(--boxes-roundness);
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
        }

        :global(.divider) {
            border:1px solid var(--theme-one-color) !important;
            background-color: var(--clear-one-color);
            margin: 0;
        }


    
    
    /*=====  End of Theme styles  ======*/
    

    
    /*=============================================
    =            mobile            =
    =============================================*/
    
    @media only screen and (max-width: 768px) {
        :global(:root) {
            --font-size-1: 1.3278855975485189vh;
            --font-size-h1: calc(var(--font-size-1) * 3.5);

            --spacing-1: 2vw;
            --navbar-height: 12.172949002217294vh; /* Not used yet */
            --footer-height: 89.72vh; /* Not used yet */
            --boxes-roundness: 6px;
            --letter-spacing: 0.39936px;

            --btn-font-size: var(--font-size-2);

            --buttons-padding: var(--spacing-2) var(--spacing-2);
        }

        :global(.icon-wrapper) {
                display: flex;
                align-items: center;
                justify-content: center;
                width: var(--spacing-2);
                margin: 0;
        }
        
    }

    /*=====  End of mobile  ======*/
    
    
    
    /*=============================================
    =            Animations            =
    =============================================*/

    @keyframes slide-fwd-bottom {
        0% {
            -webkit-transform: translateZ(160px) translateY(-100px);
                    transform: translateZ(160px) translateY(-100px);
        }
        100% {
            -webkit-transform: translateZ(0) translateY(0);
                    transform: translateZ(0) translateY(0);
        }
    }

    :global(.slide-fwd-bottom) {
        -webkit-animation: slide-fwd-bottom 0.45s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
        animation: slide-fwd-bottom 0.45s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    }
    
    
    /*=====  End of Animations  ======*/
    
    
    


    /*=============================================
    =            DEBUG            =
    =============================================*/
    
        :global(.debug) {
            border: 1px solid red !important;
        }

        :global(.debug-green) {
            border: 1px solid red;
            background-color: greenyellow;
        }
        
        :global(.debug-blue) {
            border: 1px solid red;
            background-color: blue;
        }

        :global(.debug-yellow) {
            border: 1px solid red;
            background-color: yellow;
        }
    
    
    /*=====  End of DEBUG  ======*/

</style>


<svelte:head>
    <link rel="stylesheet" href="https://use.typekit.net/tpf7knz.css">
</svelte:head>
<div id="page-content">
    <NotificationsPopup />
    <Navbar/>
    <div id="content-wrap">
        <Router {routes}/>
    </div>
    <Footer/>
</div>