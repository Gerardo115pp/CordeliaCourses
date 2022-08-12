
function attributesToJson() {
    const json_data = {};
    console.log("AttributestoJson:" + this);
    Object.entries(this).forEach(([key, value]) => {
        if (!(this[key] instanceof Function) && key[0] !== '_') {
            json_data[key] = value;
        }
    });
    return JSON.stringify(json_data);
}

export class LoginRequest {
    constructor() {
        this.email = "";
        this.password = "";
    }

    toJson = attributesToJson.bind(this);

    do = () => {
        alert(`LoginRequest: ${this.toJson()}`);
    }
}

export class SignUpRequest {
    constructor() {
        this.name = "";
        this.email = "";
        this.password = "";
    }

    toJson = attributesToJson.bind(this);

    do = () => {
        alert(`SignUpRequest: ${this.toJson()}`);
    }
}

export class PasswordRecoveryRequest {
    constructor() {
        this.email = "";
    }

    toJson = attributesToJson.bind(this);

    do = () => {
        alert(`PasswordRecoveryRequest: ${this.toJson()}`);
    }
}