<script>
    import { isMobile } from '../libs/cord_utils';
    import { link } from 'svelte-spa-router';
    import search_icon from '../icons/Lupa.svg';
    import menu_icon from '../icons/Menú.svg';
    import user_icon from '../icons/Usuario.svg';
    import store_icon from '../icons/Store.svg';

    let show_mobile_menu = false;

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
                <img src="/resources/Iconografias/LogoCR-01-1-S.webp" alt="" srcset="">
            </a>
        </div>
        <div id="cn-search-container">
            {#if !isMobile()}
                <div class="icon-wrapper">
                    
                </div>
            {:else}
                <div on:click={() => show_mobile_menu = !show_mobile_menu} class="icon-wrapper">
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
            <a href="/courses" use:link>
                <div class="cn-a-navoption icon-wrapper">{@html user_icon}</div>
            </a>
        </div>
    </nav>
</header>
{#if isMobile() && show_mobile_menu}
    <div id="cn-mobile-menu" class="scale-in-ver-top">
        <div id="cn-mm-navoptions-container">
            {#each navoptions as option}
                <div class="cn-mm-navoption">
                    <a href="{option.url}">{option.name}</a>
                </div>
            {/each}
        </div>
    </div>
{/if}

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
        width: 100%;
    }

    #cordelia-navbar {
        --cn-side-container-width: calc(var(--spacing-2) * 3.2);
        width: 50%;
        display: grid;
        grid-template: repeat(2, 1fr) / var(--cn-side-container-width) 1fr var(--cn-side-container-width) ;
        row-gap: var(--spacing-2);
    }

    #cn-cordelia-ruiz-title {
        grid-column: 1 / 4;
        display: grid;
        place-items: center;
        /* background-color: aqua; */
    }

    /* #cn-cordelia-ruiz-title h2 {
        font-size: var(--font-size-4);
        color: var(--dark-color);
        letter-spacing: 0.3489vw;
        text-align: center;
        margin: 0;
        padding: 0;
    } */

    #cn-cordelia-ruiz-title a {
        width: 30%;
    }
    
    #cn-cordelia-ruiz-title img {
        width: 100%;
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
        min-width:55ch;
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
            width: 90%;
            grid-template: 1fr / 1fr 217.219px 1fr;
            column-gap: var(--spacing-2);
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

        #cn-cordelia-ruiz-title a {
            width: 100%;
        }
        
        /* #cn-cordelia-ruiz-title h2 {
            font-size: var(--font-size-h4);
            color: var(--color-primary);
            letter-spacing: 0.3489vw;
            text-align: center;
            margin: 0;
            padding: 0;
        } */

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

        #cn-mobile-menu {
            /* display: none; */
            position: fixed;
            top: calc(var(--navbar-height) - 2px);
            left: 0;
            width: 100%;
            background-color: var(--clear-background);
            z-index: 5;
        }

        .cn-mm-navoption {
            padding: var(--spacing-3) var(--spacing-2);
        }
        
    }
</style>