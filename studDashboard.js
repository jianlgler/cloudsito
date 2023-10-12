import React from 'react';
import './studDashboard.css'; 

class StelStudDashboard extends React.Component {
    render() {
        return (
            <html>
                <head>
                    <title>StelStud 2.0</title>
                    <link
                        href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css"
                        rel="stylesheet"
                        id="bootstrap-css"
                    />
                    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
                    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
                    <link href="css/studDashboard.css" rel="stylesheet" />
                    <link
                        href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"
                        rel="stylesheet"
                        integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1"
                        crossorigin="anonymous"
                    />
                </head>

                <body className="home">
                    <div className="container-fluid display-table">
                        <div className="row display-table-row">
                            <div className="col-md-2 col-sm-1 hidden-xs display-table-cell v-align box" id="navigation">
                                <div className="logo">
                                    <a href="home.html">
                                        <img src="img/stelstud.png" alt="merkery_logo" className="visible-xs visible-sm circle-logo" />
                                    </a>
                                </div>
                                <div className="navi">
                                    <ul>
                                        <li className="active">
                                            <a href="studDashboard.html">
                                                <i className="fa fa-home" aria-hidden="true"></i>
                                                <span className="hidden-xs hidden-sm">Home</span>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#">
                                                <i className="fa fa-user" aria-hidden="true"></i>
                                                <span className="hidden-xs hidden-sm">My profile</span>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="exams.html">
                                                <i className="fa fa-tasks" aria-hidden="true"></i>
                                                <span className="hidden-xs hidden-sm">Exams</span>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="statistics.html">
                                                <i className="fa fa-bar-chart" aria-hidden="true"></i>
                                                <span className="hidden-xs hidden-sm">Statistics</span>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div className="col-md-10 col-sm-11 display-table-cell v-align">
                                <div className="row">
                                    <header>
                                        <div className="col-md-7">
                                            <div className="search hidden-xs hidden-sm">
                                                <input type="text" placeholder="Search" id="search" />
                                            </div>
                                        </div>
                                        <div className="col-md-5">
                                            <div className="header-rightside">
                                                <ul className="list-inline header-top pull-right">
                                                    <li className="hidden-xs">
                                                        <a href="#" className="add-project" data-toggle="modal" data-target="#add_project">
                                                            Add Project
                                                        </a>
                                                    </li>
                                                    <li>
                                                        <a href="#">
                                                            <i className="fa fa-envelope" aria-hidden="true"></i>
                                                        </a>
                                                    </li>
                                                    <li>
                                                        <a href="#" className="icon-info">
                                                            <i className="fa fa-bell" aria-hidden="true"></i>
                                                            <span className="label label-primary">3</span>
                                                        </a>
                                                    </li>
                                                    <li className="dropdown">
                                                        <a href="#" className="dropdown-toggle" data-toggle="dropdown">
                                                            <img src="img/stud.jpg" alt="user" />
                                                            <b className="caret"></b>
                                                        </a>
                                                        <ul className="dropdown-menu">
                                                            <li>
                                                                <div className="navbar-content">
                                                                    <span>JS Krishna</span>
                                                                    <p className="text-muted small">me@jskrishna.com</p>
                                                                    <div className="divider"></div>
                                                                    <a href="#" className="view btn-sm active">
                                                                        View Profile
                                                                    </a>
                                                                </div>
                                                            </li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </header>
                                </div>
                                <div className="user-dashboard">
                                    <h1>Welcome to StelStud dashboard, JS</h1>
                                    <div className="row">
                                        <div className="col-md-5 col-sm-5 col-xs-12 gutter">
                                            <div className="sales">
                                                <h2>Your Sale</h2>
                                                <div className="btn-group">
                                                    <button
                                                        className="btn btn-secondary btn-lg dropdown-toggle"
                                                        type="button"
                                                        data-toggle="dropdown"
                                                        aria-haspopup="true"
                                                        aria-expanded="false"
                                                    >
                                                        <span>Period:</span> Last Year
                                                    </button>
                                                    <div className="dropdown-menu">
                                                        <a href="#">2012</a>
                                                        <a href="#">2014</a>
                                                        <a href="#">2015</a>
                                                        <a href="#">2016</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div className="col-md-7 col-sm-7 col-xs-12 gutter">
                                            <div className="sales report">
                                                <h2>Report</h2>
                                                <div className="btn-group">
                                                    <button
                                                        className="btn btn-secondary btn-lg dropdown-toggle"
                                                        type="button"
                                                        data-toggle="dropdown"
                                                        aria-haspopup="true"
                                                        aria-expanded="false"
                                                    >
                                                        <span>Period:</span> Last Year
                                                    </button>
                                                    <div className="dropdown-menu">
                                                        <a href="#">2012</a>
                                                        <a href="#">2014</a>
                                                        <a href="#">2015</a>
                                                        <a href="#">2016</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script src="js/studDashboard.js"></script>
                </body>
            </html>
        );
    }
}

export default StelStudDashboard;
