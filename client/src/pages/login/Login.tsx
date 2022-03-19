import React from "react";
import "./Login.css";
import Logo from "../../assets/img/logo.png";

const Login = () => {
  return (
    <div className="lgn-cont">
      <div className="lgn-left"></div>
      <div className="lgn-right">
        <img src={Logo} alt="" className="lgn-logo" />
        <div className="lgn-form-cont">
          <div style={{width: "100%"}}>
            <div className="lgn-form-grp">
              <label className="lgn-lbl">Email Address</label>
              <input
                type="email"
                className="lgn-inp"
                placeholder="Enter Email Address"
              />
            </div>
            <div className="lgn-form-grp">
              <label className="lgn-lbl">Password</label>
              <input
                type="password"
                className="lgn-inp"
                placeholder="Enter Password"
              />
            </div>
            <div className="lgn-form-act-cont">
              <p className="lgn-fac-sm">Remember Me</p>
              <p className="lgn-fac-sm blue strong">Recover Password</p>
            </div>
            <button className="btn">Log in</button>
          </div>
          <div style={{width: "100%"}}>
            <p style={{ textAlign: "center" }}>
              <span>Don’t have an account yet? </span>
              <a href="/register" className="blue strong">Sign up!</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
