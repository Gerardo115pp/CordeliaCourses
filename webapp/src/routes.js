import Index from './pages/Index/Index.svelte';
import Redirect from './pages/Index/Redirect.svelte';
import Login from './pages/Login/Login.svelte';
import SignUp from './pages/SignUp/SignUp.svelte';
import Password from './pages/Password/Password.svelte';
import PasswordRecovery from './pages/PasswordRecovery/PasswordRecovery.svelte';
import CourseDetails from './pages/CourseDetails/CourseDetails.svelte';


const routes = {
    '/': Redirect,
    '/courses': Index,
    '/login': Login,
    '/signup': SignUp,
    '/password': Password,
    '/password-recovery': PasswordRecovery,
    '/course/:course_id': CourseDetails
}

export { routes };