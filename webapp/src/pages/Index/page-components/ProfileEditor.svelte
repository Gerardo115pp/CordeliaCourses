<script>
    import empty_profile_picture from '../../../icons/Degradado9.svg';
    import Input from '../../../components/Input.svelte';
    import FieldData, { verifyFormFields } from '../../../libs/FieldData';
    import { link } from 'svelte-spa-router';

    export let user_data = {
        username: 'ILSEESPINO',
        name: 'ilse espino',
        address: 'Monterrey, N.L.',
        email: 'tutialapendeja@gmail.com',
        phone: '34564234',
        postal_code: '45079',
    };

    let is_form_ready = false;
    const form_data = [
        new FieldData('username', /[^;\'\s\n]/, 'User', 'text'),
        new FieldData('name', /[^;\'\s\n]/, 'Nombre', 'text'),
        new FieldData('email', /[^;\'\s\n]/, 'Correo electronico', 'email'),
        new FieldData('phone', /[^;\'\s\n]/, 'Telefono', 'text'),
        new FieldData('address', /[^;\'\s\n]/, 'Direccion', 'text'),
        new FieldData('postal_code', /[^;\'\s\n]/, 'Codigo postal', 'text')
    ];

    const verifyProfileForm = () => {
        let is_valid = verifyFormFields(form_data);
        is_form_ready = is_valid;
        form_data = [...form_data];
    }


</script>
    

<div id="profile-editor-wrapper">
    <div id="pew-top-information">
        <h2 class="page-title">¡Hola, <span>{user_data.name.split(" ")[0]}</span>!</h2>
        <p id="pew-page-information">
            <span>Iniciaste sesión como {user_data.username} (¿No eres {user_data.username}? <a href="/login" use:link>Cerrar sesión</a>)</span>
            <br/>
            <span>Aquí puedes ver tus pedidos recientes, editar tu contraseña y detalles de tu cuenta.</span>
        </p>
    </div>
    <div id="pew-user-data-container">
        <div id="pew-udc-profile-picture-wrapper">
        </div>
        <div id="pew-udc-user-data">
            <h3 id="pew-udc-ud-name">{user_data.name}</h3>
            <p id="pew-udc-ud-address">{user_data.address}</p>
        </div>
    </div>
    <div id="pew-data-editor">
        <form>
            {#each form_data as field}
                <Input
                    field_data={field}
                    isClear={true}
                    isSquared={true}
                    input_label={field.name}
                    onEnterPressed={verifyProfileForm}
                    onBlur={verifyProfileForm}
                />
            {/each}
            <button class="full-two-btn">Guardar Cambios</button>
        </form>
    </div>
</div>

<style>
    
    /*=============================================
    =            Top information            =
    =============================================*/
    
        #pew-top-information h2 {
            font-size: var(--font-size-h1);
            text-transform: capitalize;
        }
        
        #pew-top-information h2 span {
            color: var(--theme-five-color);
        }

        #pew-page-information {
            font-size: var(--font-size-2);
            color: var(--dark-light-color);
        }
        
        #pew-page-information a {
            color: inherit;
        }
    
    /*=====  End of Top information  ======*/
    
    
    /*=============================================
    =            User data            =
    =============================================*/
        
        #pew-user-data-container {
            display: flex;
            margin: var(--spacing-h1) 0;
            align-items: center;
        }

        #pew-udc-profile-picture-wrapper {
            --profile-picture-size: 25vh;
            width: var(--profile-picture-size);
            height: var(--profile-picture-size);
            margin-right: var(--spacing-h1);
            background: var(--theme-light-five-color);
            border-radius: 50%;
            z-index: 2;
        }

        #pew-udc-user-data h3 {
            font-size: var(--font-size-h2);

        }

        #pew-udc-user-data p {
            font-size: var(--font-size-2);
            color: var(--dark-light-color);
        }
        
    /*=====  End of User data  ======*/
    
    
    /*=============================================
    =            User data editor            =
    =============================================*/
    
    #pew-data-editor form{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-gap: var(--spacing-h2);
    }

    #pew-data-editor form button {
        width: 70%;
    }
    
    
    /*=====  End of User data editor  ======*/
    
    

</style>