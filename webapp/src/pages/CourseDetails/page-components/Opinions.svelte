<script>
    import { PostNewOpinion, GetCourseOpinionsRequest} from  '../../../libs/HttpRequests';
    import Input from "../../../components/Input.svelte";
    import FieldData from "../../../libs/FieldData";
    import cordelia_storage from '../../../libs/local_storage';
    import { newNotification } from '../../../components/Notifications/events';
    import { onMount } from 'svelte';

    export let class_id = undefined;
    export let course_id = undefined;
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

    onMount(() => {
        requestClassMessages();
    })

    const new_opinion = new FieldData("new-opinion", /[.\n]{1, 245}/, "opinion-body");
    new_opinion.placeholder = "que opinas?";

    const date_formatter = new Intl.DateTimeFormat("es-ES", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric"
    });

    const requestClassMessages = () => {
        if (class_id === undefined|| course_id === undefined) {
            console.error("class_id or course_id is undefined");
            return;
        }

        const request = new GetCourseOpinionsRequest(cordelia_storage.Token, course_id, class_id);

        const on_success = opinions_data => {
            console.log(opinions_data);
            opinions = opinions_data;
        }

        const on_error = error_code => {
            newNotification(`Error desconocido: ${error_code}`);
        }

        request.do(on_success, on_error);
    }

    const postOpinion = () => {
        const opinion_body = new_opinion.getFieldValue();
        if (opinion_body.length === 0) {
            return;
        }

        if (opinion_body.length > 245) {
            newNotification("El mensaje no puede tener mas de 244 caracteres");
            return;
        }

        const request = new PostNewOpinion(cordelia_storage.Token, course_id, class_id);
        console.log(request._token)
        request.body = opinion_body;
        new_opinion.clear();
        
        const on_success = () => {
            requestClassMessages();
        }

        const on_error = error_code => {
            newNotification(`Error desconocido: ${error_code}`);
        }

        request.do(on_success, on_error);
    }
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
                    onEnterPressed={postOpinion}
                    input_padding="0.5rem 1rem"
                    autocomplete="off"
                    field_data={new_opinion}
                />
            </div>
            <button on:click={postOpinion}  class="full-btn">Enviar</button>
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