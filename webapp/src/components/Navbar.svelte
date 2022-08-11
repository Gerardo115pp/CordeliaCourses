<script>
    import search_icon from '../icons/Lupa.svg';
    import user_icon from '../icons/Usuario.svg';
    import store_icon from '../icons/Store.svg';
</script>

<header id="cordelia-navbar-wrapper">
    <nav id="cordelia-navbar">
        <div id="cn-cordelia-ruiz-title">
            <a href="https://cordeliaruiz.com">
                <h2>Cordelia Ruiz</h2>
            </a>
        </div>
        <div id="cn-search-container">
            <div class="icon-wrapper">
                {@html search_icon}
            </div>
        </div>
        <div id="cn-navoptions-wrapper">
            <div id="cn-navoptions-container">
                <div class="cn-navoption">
                    <a href="https://cordeliaruiz.com/acerca-de/">acerca de</a>
                </div>
                <div class="cn-navoption">
                    <a href="https://cordeliaruiz.com/tienda-2/">tienda</a>
                </div>
                <div class="cn-navoption">
                    <a href="https://cordeliaruiz.com/contacto/">contacto</a>
                </div>
            </div>
        </div>
        <div id="cn-aside-navoptions">
            <div class="cn-a-navoption icon-wrapper">{@html store_icon}</div>
            <div class="cn-a-navoption icon-wrapper">{@html user_icon}</div>
        </div>
    </nav>
</header>

<style>

    /* DEBUG */
    /* 
    * {
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
        width: 18%;
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
</style>