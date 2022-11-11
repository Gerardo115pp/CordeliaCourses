// import { CheckToken } from '../types/Http_messages';
import { push } from 'svelte-spa-router';
import cordelia_storage from './local_storage';
import Cookies from 'js-cookie';

export const isMobile = () => {
    let is_mobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    if (!is_mobile && window.innerWidth < 768) {
        is_mobile = true;
    }
    
    return is_mobile;
}

const CORDELIA_TOKEN = "cordelia-token"; // cookie name
export const isLoggedIn = (redirect=true) => {
    let json_web_token = Cookies.get(CORDELIA_TOKEN);
    let is_logged_in = json_web_token !== undefined;

    if (!is_logged_in && redirect) {
        push("/login");
    }

    return is_logged_in;
}

export const getToken = () => {
    return Cookies.get(CORDELIA_TOKEN);
}

export const getUrlPARAM = key => {
    let url_string = window.location.href; // 
    url_string = url_string.replace(/\/.{0,3}#/, ""); // remove #
    let url = new URL(url_string);
    return url.searchParams.get(key);

}

export const signOut = () => {
    cordelia_storage.removeToken();
    push('/login');
}

export const validateToken = () => {
    // let token = getToken();
    
    // if (token === undefined) {
    //     push("/login");
    // }

    // const request = new CheckToken(token);
    // request.do(response => { 
    //     if(response.status >= 400 && response.status < 500) {
    //         console.warn("Token is not valid");
    //         Cookies.remove(CORDELIA_TOKEN);
    //         window.queueMicrotask(() => push("/login"));
    //     }
    // })
}
