<script>
    import { onMount } from 'svelte';
    import { validateToken } from '../../libs/login-utils';

    onMount(() => {
        validateToken();
    });
</script>

<h2>soy la puta</h2>