<script>
    export let notification_text = "";
</script>

<div id="notification-bubble-wrapper">
    {#if notification_text !== ""}
        <div id="notification-bubble" class="slide-fwd-bottom">
            <span class="notification-content">{notification_text}</span>
            <button on:click={() => notification_text = ''} class="nb-close-btn">X</button>
        </div>
    {/if}
</div>

<style>

    #notification-bubble-wrapper {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 5;
        display: grid;
        padding: var(--spacing-3) ;
        place-items: center;
    }

    #notification-bubble {
        box-sizing: border-box;
        display: flex;
        width: 50%;
        background: var(--theme-five-color);
        border-radius: var(--boxes-roundness);
        padding: var(--spacing-2) var(--spacing-h2);
        color: var(--clear-color);
        justify-content: space-between;
        align-items: center;
        box-shadow: var(--boxes-shadow);
    }

    .notification-content {
        cursor: default;
        /* user-select: none; */
        font-size: var(--font-size-2);
        text-transform: uppercase;
        font-weight: 500;
    }

    #notification-bubble .nb-close-btn {
        background: transparent;
        border: none;
        color: var(--clear-color);
        font-size: var(--font-size-2);
        font-weight: 500;
        transition: all 0.2s ease-in;
    }

    #notification-bubble .nb-close-btn:hover {
        color: var(--theme-light-five-color);
    }

    @media only screen and (max-width: 768px) {
        #notification-bubble-wrapper {
            padding: var(--spacing-2) 0 ;
        }

        #notification-bubble {
            width: 95%;
            padding: var(--spacing-2);
        }

        .notification-content {
            max-width: 80%;
            font-size: var(--font-size-1);
        }
    }

</style>
