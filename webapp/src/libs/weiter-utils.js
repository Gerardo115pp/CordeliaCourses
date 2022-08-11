import Cookies from 'js-cookie';
import { push } from 'svelte-spa-router';
import { CheckToken } from '../types/Http_messages';

const WEITER_RESTAURANT_TOKEN = "weiter-restaurant-token"; // cookie name
export const isLoggedIn = (redirect=true) => {
    let json_web_token = Cookies.get(WEITER_RESTAURANT_TOKEN);
    let is_logged_in = json_web_token !== undefined;

    if (!is_logged_in && redirect) {
        push("/login");
    }

    return is_logged_in;
}

export const getToken = () => {
    return Cookies.get(WEITER_RESTAURANT_TOKEN);
}

export const getUrlPARAM = key => {
    let url_string = window.location.href; // 
    url_string = url_string.replace(/\/.{0,3}#/, ""); // remove #
    let url = new URL(url_string);
    return url.searchParams.get(key);

}

export const validateToken = () => {
    let token = getToken();
    
    if (token === undefined) {
        push("/login");
    }

    const request = new CheckToken(token);
    request.do(response => { 
        if(response.status >= 400 && response.status < 500) {
            console.warn("Token is not valid");
            Cookies.remove(WEITER_RESTAURANT_TOKEN);
            window.queueMicrotask(() => push("/login"));
        }
    })
}
