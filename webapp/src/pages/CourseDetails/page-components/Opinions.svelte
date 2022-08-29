<script>

    import Input from "../../../components/Input.svelte";
    import FieldData from "../../../libs/FieldData";

    // export let class_id = "1";
    export let opinions = [
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
        {
            username: "Some happy fellow",
            body: "Some very happy opinion from some very happy fellow about this very happy course",
            isodate: "2020-07-10 15:00:00.000"
        },
    ]

    const new_opinion = new FieldData("new-opinion", /[.\n]+/, "opinion-body");
    new_opinion.placeholder = "que opinas?";

    const date_formatter = new Intl.DateTimeFormat("es-ES", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric"
    });
</script>

<div id="opinions">
    <h2>Opiniones</h2>
    <div id="opinions-container">
        {#each opinions as opinion}
            <div class="opinion">
                <div class="opinion-header">
                    <div class="opinion-header-left">
                        <div class="opinion-header-left-text">
                            <h3>{opinion.username}</h3>
                            <p>{date_formatter.format(new Date(opinion.isodate).getTime())}</p>
                        </div>
                    </div>
                </div>
                <div class="opinion-body">
                    <p>{opinion.body}</p>
                </div>
            </div>
        {/each}
    </div>
    <div id="opinion-writter-wrapper">
        <div id="opinion-writter">
            <div id="writter-wrapper">
                <Input 
                    isClear
                    
                    input_padding="0.5rem 1rem"
                    autocomplete="off"
                    field_data={new_opinion}
                />
            </div>
            <button class="full-btn">Enviar</button>
        </div>
    </div>
</div>

<style>
    #opinions {
        width: 100%;
    }
    #opinions > h2 {
        font-family: var(--font-texts);
        font-size: var(--font-size-h4);
        color: var(--theme-five-color);
        font-weight: 600;
        margin-bottom: var(--spacing-2);
    }

    #opinions-container {
        width: 100%;
        height: calc(3 * var(--spacing-h3));
        overflow-y: scroll;
        padding: var(--spacing-2) var(--spacing-2) 0  var(--spacing-2);
        border-top: 1px solid var(--placeholder-color);
    }



    /* Opinion */

    .opinion:not(:last-child) {
        margin-bottom: var(--spacing-h3);
    }

    .opinion-header-left-text {
        color: var(--theme-five-color);
    }

    .opinion-header-left-text h3 {
        width: max-content;
        display: inline;
        font-family: var(--font-texts);
        font-size: var(--font-size-2);
        font-weight: 500;
    }

    .opinion-header-left-text h3::after {
        content: " - ";
    }

    .opinion-header-left-text p {
        width: max-content;
        display: inline;
        font-family: var(--font-texts);
        font-size: var(--font-size-1);
        font-weight: 400;
    }

    .opinion-body {
        box-sizing: content-box;
        font-size: var(--font-size-2);
        color: var(--dark-light-color);
        padding: var(--spacing-2) var(--spacing-2) 0 var(--spacing-2);
    }

    /* Opinion writter */

    #opinion-writter-wrapper {
        width: 100%;
        border-top: 1px solid var(--placeholder-color);
        padding-top: var(--spacing-2);
    }

    #opinion-writter {
        width: 100%;
        display: grid;
        grid-template-columns: minmax(12ch, 60ch) minmax(10ch, 20ch);
        column-gap: var(--spacing-h2);
        /* place-items: center; */
        padding: 0 0 0 var(--spacing-2);
    }

    #writter-wrapper {
        grid-column: 1 / 2;
    }

    #opinion-writter button {
        grid-column: 2 / 3;
    }
</style>