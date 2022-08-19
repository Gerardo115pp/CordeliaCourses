<script>
    import empty_profile_picture from '../../../icons/Degradado9.svg';
    import Input from '../../../components/Input.svelte';
    import FieldData, { verifyFormFields } from '../../../libs/FieldData';
    import { link } from 'svelte-spa-router';
    import jwt_decode from 'jwt-decode';
    import { onMount } from 'svelte';
    import { getToken } from '../../../libs/cord_utils';

    export let user_data = {
        id: "customer-uuid-example",
        email: "no email",
        name: "no",
        last_name: "name"
    };

    onMount(() => {
        const token = getToken();
        const decoded = jwt_decode(token);
        user_data = decoded;
    });


</script>
    

<div id="profile-editor-wrapper">
    <div id="pew-top-information">
        <h2 class="page-title">¡Hola, <span>{user_data.name}</span>!</h2>
        <p id="pew-page-information">
            <span>Iniciaste sesión como <span>{user_data.name+user_data.last_name}</span> (¿No eres <span>{user_data.name+user_data.last_name}</span>? <a href="/login" use:link>Cerrar sesión</a>)</span>
            <br/>
            <span>Aquí puedes ver tus pedidos recientes, editar tu contraseña y detalles de tu cuenta.</span>
        </p>
    </div>
    <div id="pew-user-data-container">
        <div id="pew-udc-profile-picture-wrapper">
        </div>
        <div id="pew-udc-user-data">
            <h3 id="pew-udc-ud-name">{`${user_data.name} ${user_data.last_name}`}</h3>
            <p id="pew-udc-ud-address">{user_data.email}</p>
        </div>
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
        
        #pew-page-information>span>span {
            text-transform: uppercase;
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
    
    
    /*=====  End of User data editor  ======*/
    
    @media only screen and (max-width: 768px) {

        #profile-editor-wrapper {
            padding: 0 var(--spacing-2);
        }

        #pew-user-data-container {
            margin: var(--spacing-h3) 0;
        }

        #pew-udc-profile-picture-wrapper {
            --profile-picture-size: 17vw;

            width: var(--profile-picture-size);
            height: var(--profile-picture-size);
            margin-right: var(--spacing-3);
            border-radius: 50%;
            z-index: 2;
        }
        
    }

</style>