<script>
    import { onMount } from 'svelte';
    import { validateToken } from '../../libs/login-utils';

    onMount(() => {
        validateToken();
    });
</script>

<h2>adios</h2>