import { GetDataVersion } from "./HttpRequests";

class CordeliaStorage {
    constructor() {
        this.token = "";
        this.data_version = 1;
        this.state = {
            courses: [],
            courses_details: {}
        }
        
        this.loadData();
        this.checkDataVersion(); // async, uses fetch and if the data version is different, it will update the data 
        console.log("CordeliaStorage constructor initialized");
    }

    
    /*=============================================
    =            Propertys            =
    =============================================*/
    
    get Token() {
        return this.token;
    }

    set Token(token) {
        if (token !== this.token) {
            this.reset(0);
        }
        this.token = token;
        this.saveData();
    }

    get Courses() {
        return this.state.courses;
    }

    set Courses(courses) {
        this.state.courses = courses;
        this.saveData();
    }

    getCoursesDateils = (name) => {
        return this.state.courses_details[name];
    }

    setCourseDetails = (name, details) => {
        this.state.courses_details[name] = details;
        this.saveData();
    }
    
    
    /*=====  End of Propertys  ======*/
    
    


    checkDataVersion = () => {
        // alert("checkDataVersion");
        const request = new GetDataVersion();
        request.do(data => {
            console.log(`${data.data_version}:${typeof data.data_version} === ${this.data_version}:${typeof this.data_version}`);
            if (data.data_version !== this.data_version) {
                this.reset(data.data_version);
            }
        });
    }

    loadData = () => {
        const courses = localStorage.getItem("courses");
        if (courses) {
            try {
                this.state.courses = JSON.parse(courses);
            } catch (error) {
                console.log(`Error parsing courses: ${error}`);
                this.state.courses = [];
            }
        }

        const courses_details = localStorage.getItem("courses_details");
        if (courses_details) {
            try {
                this.state.courses_details = JSON.parse(courses_details);
            } catch (error) {
                console.log(`Error parsing courses_details: ${error}`);
                this.state.courses_details = {};
            }
        }

        const data_version = localStorage.getItem("data_version");
        if (data_version) {
            try {
                this.data_version = JSON.parse(data_version);
            } catch (error) {
                console.log(`Error parsing data_version: ${error}`);
                this.state.data_version = 1;
            }
        }

        const token = localStorage.getItem("token");
        if (token) {
            try {
                this.token = JSON.parse(token);
            } catch (error) {
                console.log(`Error parsing token: ${error}`);
                this.token = "";
            }
        }
    }

    reset = data_version => {
        this.state = {
            courses: [],
            courses_details: {}
        }
        this.data_version = data_version;
        this.saveData();
    }

    removeToken = () => {
        this.token = "";
        this.saveData();
    }

    saveData = () => {
        localStorage.setItem("courses", JSON.stringify(this.state.courses));
        localStorage.setItem("courses_details", JSON.stringify(this.state.courses_details));
        localStorage.setItem("data_version", JSON.stringify(this.data_version));
        localStorage.setItem("token", JSON.stringify(this.token));
    }
}

const cordelia_storage = new CordeliaStorage();

export default cordelia_storage;