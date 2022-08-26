<script>
    import { newNotification } from '../../components/Notifications/events';
    import CordeliaPants from '../../components/PantsBackground.svelte';
    import FieldData, { verifyFormFields, FieldStates } from '../../libs/FieldData';
    import { ChangePasswordRequest } from '../../libs/HttpRequests';
    import { getUrlPARAM } from '../../libs/cord_utils';
    import Input from '../../components/Input.svelte';
    import { push } from 'svelte-spa-router';
    import { onMount } from 'svelte';
    
    let password_recovery_token = getUrlPARAM('token');
    const change_password_request = new ChangePasswordRequest();
    let is_form_ready = false;

    let form_data = [
        new FieldData('customer_password', /[^;\s\n]{8,}/, 'Contraseña', 'password'),
        new FieldData('customer_password_confirm', /[^;\s\n]{8,}/, 'Confirmar contraseña', 'password')
    ];
    form_data[0].placeholder = "Contraseña de 8+ caracteres";
    form_data[1].placeholder = "";

    // Link FormData to login_request
        $: change_password_request.password = form_data[0].getFieldValue();
        $: change_password_request.password_confirm = form_data[1].getFieldValue();
    //

    onMount(() => {
        change_password_request._token = password_recovery_token;
    });

    const verifyPasswordRecoveryForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        if (form_data[0].getFieldValue() !== form_data[1].getFieldValue() && form_data[1].getFieldValue() !== "") {
            is_form_ready = false;
            newNotification("Las contraseñas no coinciden");
            form_data[1].state = FieldStates.HAS_ERRORS;
        }
        form_data = [...form_data];
    }

    const change_password = () => {
        if (is_form_ready) {
            const on_success = response => {
                newNotification("Contraseña cambiada con exito");
                push('/login');
            };

            const on_error = status_code => {
                switch (status_code) {
                    case 401:
                        newNotification("Token invalido");
                        break;
                    case 408:
                        newNotification("Link expirado");
                        break;
                    case 406:
                        newNotification("La contraseña no cumple con los requisitos");
                        break;
                    case 422:
                        newNotification("Parece que el link ya fue usado");
                        break;
                    default:
                        newNotification(`Error inesperado: ${status_code}`);
                        break;
                }
            };
            
            change_password_request.do(on_success, on_error);
        }
    }

</script>

<CordeliaPants>
    <div slot="form" id="ccp-change-password-form">
        <h2 class="page-title">Cambiar contraseña</h2>
        <div id="ccp-pc-fields-container">
            {#each form_data as field}
                <div class="ccp-pc-fc-field-wrapper">
                    <Input
                        field_data={field}
                        isClear={true}
                        isSquared={true}
                        input_color="var(--dark-light-color)"
                        input_dark_color="var(--theme-color)"
                        input_label={field.name}
                        show_placeholder={true}
                        onEnterPressed={verifyPasswordRecoveryForm}
                        onBlur={verifyPasswordRecoveryForm}
                    />
                </div>
            {/each}
        </div>
        <div id="ccp-pc-form-controls">
            <button on:click={change_password} id="ccp-pc-login-btn" class="full-btn">Cambiar contraseña</button>
        </div>
    </div>
</CordeliaPants>

<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */


    #ccp-change-password-form {
        width: 75%;
    }

    #ccp-pc-fields-container .ccp-pc-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #ccp-pc-form-controls {
        display: grid;
        height: 20%;
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }

    
    @media only screen and (max-width: 768px) {
        #ccp-change-password-form {
            box-sizing: content-box;
            padding: var(--spacing-1) 0;
            width: 90%;
        }

        #ccp-pc-form-controls {
            grid-template: auto / repeat(1, 1fr);
        }

        #ccp-pc-form-controls * {
            width: 80%;
        }
    }
</style>

