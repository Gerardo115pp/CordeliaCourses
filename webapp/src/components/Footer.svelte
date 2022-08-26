<script>
    import instagram_icon from "../icons/Instagram.svg";
    import facebook_icon from "../icons/Facebook.svg";

    const footer_top_navoptions = {
        "acerca de": {
            "url": "https://cordeliaruiz.com/acerca-de/",
            "suboptions": {}
        },
        "tienda": {
            "url": "https://cordeliaruiz.com/tienda/",
            "suboptions": {
                "servicios": "https://cordeliaruiz.com/servicios-2/",
                "cursos": "https://cordeliaruiz.com/cursos-2/",
                "e-books": "https://cordeliaruiz.com/e-books/",
            }
        },
        "contacto": {
            "url": "https://cordeliaruiz.com/contacto/",
            "suboptions": {}
        }
    }
    

</script>

<footer id="cordelia-footer">
    <div id="cordelia-brand-wrapper">
        <div id="cbw-wrapper">
            <h3 class="cordelia-ruiz-brand-label">cordelia ruiz</h3>
            <div id="cbw-socials-wrapper">
                <a href="https://www.instagram.com/cordeliaruiz/" target="_blank" id="cbw-sw-instagram" class="icon-wrapper">
                    {@html instagram_icon}
                </a>
                <a href="https://www.facebook.com/cordelia.personalstylist/" target="_blank" id="cbw-sw-facebook" class="icon-wrapper">
                    {@html facebook_icon}
                </a>
            </div>
        </div>
    </div>
    <div id="cordelia-nav-footer">
        <div id="cnf-content-wrapper">
            <div id="cnf-cw-navoptions-container">
                {#each Object.keys(footer_top_navoptions) as navoption}
                    <div class="cnf-cw-navoption-wrapper">
                        <a href="{footer_top_navoptions[navoption].url}">{navoption}</a>
                        {#if footer_top_navoptions[navoption].suboptions}
                            <div class="cnf-cw-navoption-suboptions-wrapper">
                                {#each Object.keys(footer_top_navoptions[navoption].suboptions) as suboption}
                                    <a href="{footer_top_navoptions[navoption].suboptions[suboption]}">{suboption}</a>
                                {/each}
                            </div>
                        {/if}
                    </div>
                {/each}
            </div>
            <div id="cnf-cw-bottom-options">
                <div id="cnf-cw-bo-wrapper">
                    <a href="https://cordeliaruiz.com/terminos-y-condiciones/">términos y condiciones</a>
                    <a href="https://cordeliaruiz.com/aviso-de-privacidad/">aviso de privacidad</a>
                </div>
            </div>
        </div>
    </div>
</footer>

<style>
    #cordelia-footer {
        --footer-top-padding: 12%;
        
        box-sizing: border-box;
        display: grid;
        background: var(--theme-color);
        grid-template-columns: repeat(2, 1fr);
        color: var(--theme-three-color);
        min-height: var(--footer-height);
    }

    
    /*=============================================
    =            Cordelia Brand            =
    =============================================*/
    
    
        #cordelia-brand-wrapper      {
                display: flex;
                justify-content: center;
                padding: var(--footer-top-padding);
                border-right: 1px solid var(--theme-three-color);
            }

        #cbw-wrapper {
            height: 36%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        #cbw-wrapper h3 {
            font-size: 35px;
            text-transform: uppercase;
        }
        
        #cbw-socials-wrapper {
            display: flex;
            align-items: center;    
        }

        #cbw-socials-wrapper a:not(:last-child) {
            margin-right: var(--spacing-4);
        }

        :global(#cbw-socials-wrapper a svg) {
            fill: var(--theme-three-color);
        }

        #cbw-sw-instagram {
            width: calc(var(--spacing-3) + calc(var(--spacing-3) * 0.2));
        }

    /*=====  End of Cordelia Brand  ======*/
    
    

    
    /*=============================================
    =            Footer Navs            =
    =============================================*/
    
    
    #cordelia-nav-footer {
        display: flex;
        padding: var(--footer-top-padding) 0 0 10%;
        z-index: 5;
    }
    
    #cnf-content-wrapper {
        display: flex;
        width: 45%;
        height: 90%;
        flex-direction: column;
        justify-content: space-between;

    
    }

    #cnf-content-wrapper a{
        color: var(--theme-three-color);
    }

    #cnf-cw-navoptions-container {
        display: flex;
        justify-content: space-between;
    }

    .cnf-cw-navoption-suboptions-wrapper {
        display: grid;
        grid-template-columns: 1fr;
        margin-top: var(--spacing-3);
        gap: var(--spacing-3);
    }

    .cnf-cw-navoption-suboptions-wrapper a {
        font-weight: 300;
        text-transform: capitalize;
    }


    #cnf-cw-bottom-options {
        width: 100%;
    }
    
    #cnf-cw-bo-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    #cnf-cw-bo-wrapper a {
        font-weight: 300;
    }
    /*=====  End of Footer Navs  ======*/
    
    @media only screen and (max-width: 768px) {
        #cordelia-footer {
            --footer-top-padding: 27vw;
            grid-template-columns: 1fr;
        }

        #cordelia-brand-wrapper {
            padding: var(--footer-top-padding) 0;
            border-right: none;
            border-bottom: 1px solid var(--theme-three-color);
        }

        #cbw-wrapper {
            height: 66%;
        }

        #cbw-socials-wrapper {
            display: flex;
            width: max-content;
            margin: var(--spacing-3) auto 0;
            align-items: center;    
        }

        #cnf-content-wrapper {
            width: 100%;
        }
        
        #cnf-cw-navoptions-container {
            flex-direction: column;
            justify-content: space-between;
        }
        
        #cnf-cw-navoptions-container .cnf-cw-navoption-wrapper {
            margin-bottom: var(--spacing-3);
        }
        
        #cnf-cw-navoptions-container .cnf-cw-navoption-suboptions-wrapper {
            grid-template-columns: 1fr;
        }
        
        #cnf-cw-navoptions-container .cnf-cw-navoption-suboptions-wrapper a {
            margin-bottom: var(--spacing-3);
        }
        
        #cnf-cw-bottom-options {
            flex-direction: column;
            justify-content: space-between;
        }
        
        #cnf-cw-bo-wrapper {
            flex-direction: column;
            justify-content: space-between;
        }

        #cnf-cw-bo-wrapper a {
            margin-bottom: var(--spacing-3);
        }
    }
</style>