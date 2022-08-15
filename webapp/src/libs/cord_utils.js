export const isMobile = () => {
    let is_mobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    
    if (!is_mobile && window.innerWidth < 768) {
        is_mobile = true;
    }
    
    return is_mobile;
}