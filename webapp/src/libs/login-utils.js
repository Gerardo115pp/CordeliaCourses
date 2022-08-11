import { push } from 'svelte-spa-router';

export const validateToken = (redirect=true) => {
    // TODO: validate token
    if (redirect) {
        push('/login');
    }
    return true;
}