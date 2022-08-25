<script>
    import FieldData, { verifyFormFields } from '../../libs/FieldData';
    import { PasswordRecoveryRequest } from '../../libs/HttpRequests';
    import Input from '../../components/Input.svelte';
    import CordeliaPants from '../../components/PantsBackground.svelte';
    import { newNotification } from '../../components/Notifications/events';
    import { push } from 'svelte-spa-router';

    const password_recovery_request = new PasswordRecoveryRequest();
    let is_form_ready = false;

    let form_data = [
        new FieldData('customer_email', /[^;\'\s\n]/, 'Correo electronico', 'email')
    ]

    // Link FormData to login_request
        $: password_recovery_request.email = form_data[0].getFieldValue();
    // 

    const verifyPasswordRecoveryForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        form_data = [...form_data];
    }

    const sendRecoveryLink = () => {
        if (is_form_ready) {
            const on_success = response => {
                newNotification("Se ha enviado un correo electronico con el enlace para recuperar su contraseña");
            }

            const on_error = status_code => {
                if (status_code === 400) {
                    newNotification("El correo electronico no es valido");
                } else {
                    newNotification(`Ha ocurrido un error, por favor intente mas tarde(${status_code})`);
                }
            }

            password_recovery_request.do(on_success, on_error);
        }
    }

</script>

<CordeliaPants>
    <div slot="form" id="prf-pw-recovery-form">
        <h2 class="page-title">¿OLVIDASTE TU CONTRASEÑA?</h2>
        <h3 class="password-page-subtitle">No te preocupes, te enviaremos un link para reestablecerla</h3>
        <div id="prf-lf-fields-container">
            {#each form_data as field}
                <div class="prf-lf-fc-field-wrapper">
                    <Input
                        field_data={field}
                        isClear={true}
                        isSquared={true}
                        input_label={field.name}
                        onEnterPressed={verifyPasswordRecoveryForm}
                        onBlur={verifyPasswordRecoveryForm}
                    />
                </div>
            {/each}
        </div>
        <div id="prf-lf-form-controls">
            <button on:click={sendRecoveryLink} id="prf-lf-login-btn" class="full-btn">Enviar link</button>
        </div>
    </div>
</CordeliaPants>


<style>
    /* DEBUG */
    /* * {
        border: 1px solid red;
    } */


    #prf-pw-recovery-form {
        width: 75%;
    }

    .password-page-subtitle {
        font-family: var(--font-texts);
        font-size: var(--font-size-3);
        color: var(--dark-light-color);
        text-transform: none;
    }

    #prf-lf-fields-container .prf-lf-fc-field-wrapper{
        margin: var(--spacing-h3) 0;
    }

    #prf-lf-form-controls {
        display: grid;
        width: 60%;
        height: 20%;
        margin-top: var(--spacing-h2);
        grid-template: repeat(2, 1fr) / repeat(2, 1fr);
        gap: var(--spacing-3) var(--spacing-3);
    }

    @media only screen and (max-width: 768px) {
        #prf-pw-recovery-form {
            box-sizing: content-box;
            padding: var(--spacing-1) 0;
            width: 90%;
        }

        .password-page-subtitle {
            margin: var(--spacing-h3) 0;
        }

        #prf-lf-form-controls {
            width: 90%;
            grid-template: auto / repeat(1, 1fr);
            gap: 0;
            place-items: center;
        }

        #prf-lf-form-controls * {
            width: 100%;
            margin: 0 auto;
        }
    }
    
</style>

