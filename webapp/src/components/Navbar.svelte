<script>
    import { isMobile } from '../libs/cord_utils';
    import search_icon from '../icons/Lupa.svg';
    import menu_icon from '../icons/Menú.svg';
    import user_icon from '../icons/Usuario.svg';
    import store_icon from '../icons/Store.svg';

    const navoptions = [
        {
            name: 'Acerca de',
            url: 'https://cordeliaruiz.com/acerca-de/'
        },
        {
            name: 'tienda',
            url: 'https://cordeliaruiz.com/tienda-2/'
        },
        {
            name: 'Acerca de',
            url: 'https://cordeliaruiz.com/contacto/'
        },
        {
            name: 'serie tendencias',
            url: 'https://cordeliaruiz.com/serietendencias/'
        },
    ]
</script>

<header id="cordelia-navbar-wrapper">
    <nav id="cordelia-navbar">
        <div id="cn-cordelia-ruiz-title">
            <a href="https://cordeliaruiz.com">
                <h2>Cordelia Ruiz</h2>
            </a>
        </div>
        <div id="cn-search-container">
            {#if !isMobile()}
                <div class="icon-wrapper">
                    {@html search_icon}
                </div>
            {:else}
                <div class="icon-wrapper">
                    {@html menu_icon}
                </div>
            {/if}
        </div>
        <div id="cn-navoptions-wrapper">
            {#if !isMobile()}
                <div id="cn-navoptions-container">
                    {#each navoptions as option}
                        <div class="cn-navoption">
                            <a href="{option.url}">{option.name}</a>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>
        <div id="cn-aside-navoptions">
            <div class="cn-a-navoption icon-wrapper">{@html store_icon}</div>
            <div class="cn-a-navoption icon-wrapper">{@html user_icon}</div>
        </div>
    </nav>
</header>

<style>

    /* DEBUG */
    
    /* * {
        border: 1px solid red;
    } */

    #cordelia-navbar-wrapper {
        display: grid;
        place-items: center;
        height: var(--navbar-height);
        max-width: 100%;
        width: 100vw;
    }

    #cordelia-navbar {
        --cn-side-container-width: calc(var(--spacing-2) * 3.2);
        width: 80%;
        display: grid;
        grid-template: repeat(2, 1fr) / var(--cn-side-container-width) 1fr var(--cn-side-container-width) ;
        row-gap: var(--spacing-2);
    }

    #cn-cordelia-ruiz-title {
        grid-column: 1 / 4;
    }

    #cn-cordelia-ruiz-title h2 {
        font-size: var(--font-size-h3);
        color: var(--color-primary);
        letter-spacing: 0.3489vw;
        text-align: center;
        margin: 0;
        padding: 0;
    }

    #cn-search-container .icon-wrapper {
        cursor: pointer;
    }
    
    #cn-navoptions-wrapper {
        display: flex;
        justify-items: center;
        align-items: center;
    }

    #cn-navoptions-container {
        width: 28%;
        display: flex;
        margin: 0 auto;
        justify-content: space-around;
    }

    #cn-aside-navoptions {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    #cn-aside-navoptions .icon-wrapper {
        cursor: pointer;
        width: calc(var(--spacing-2) + calc(var(--spacing-2) * 0.2));
    }

    @media only screen and (max-width: 768px) {
        #cordelia-navbar {
            --cn-side-container-width: calc(var(--spacing-2) * 3.2);
            grid-template: 1fr / var(--cn-side-container-width) 1fr var(--cn-side-container-width) ;
        }

        #cn-search-container {
            display: flex;
            width: var(--spacing-2);
            grid-column: 1 / 2;
            justify-content: center;
            align-items: center;
        }

        #cn-cordelia-ruiz-title {
            grid-column: 2 / 3;
            grid-row: 1 / 2;
        }
        
        #cn-cordelia-ruiz-title h2 {
            font-size: var(--font-size-h4);
            color: var(--color-primary);
            letter-spacing: 0.3489vw;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        #cn-aside-navoptions {
            grid-column: 3 / 4;
            grid-row: 1 / 2;
        }
        
        #cn-aside-navoptions .icon-wrapper {
            cursor: pointer;
            width: var(--spacing-2);
        }

        #cn-navoptions-wrapper {
            display: none;
        }
        
    }
</style>