import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:apartly/utilities/constants.dart';
import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter_login/flutter_login.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LoginPage extends StatelessWidget {
//  final prefs = await SharedPreferences.getInstance();
  void _handleTap() {}

  Future<String> _handleLogin(String name, String Id) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString('name', name);
    await prefs.setString('Id', Id).then((value) => {
      //navigate to maiin page

    });
    return "Logged In";
  }

//  _updateLoginPref() async {
//    SharedPreferences prefs = await SharedPreferences.getInstance();
//    String name = (prefs.getString('name'));
//
////    print('Pressed $counter times.');
//    await prefs.setInt('counter', counter);
//  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Scaffold(
        backgroundColor: Constants.themePurple,
        body: SafeArea(
          child: Stack(
            children: <Widget>[
              FlutterLogin(
                messages: LoginMessages(
                    usernameHint: "What's your name?",
                    passwordHint: "Account ID",
                    forgotPasswordButton: 'Forgot ID?'),
                theme: LoginTheme(
                    cardTheme: CardTheme(elevation: 5),
                    titleStyle: TextStyle(
                      fontSize: 30,
                    ),
                    primaryColor: Constants.themePurple,
                    pageColorLight: Constants.themePurple),
                title: 'Login',

                logoTag: 'Getting it done',
                onLogin: (data) async {
                  return _handleLogin(data.name, data.password);
                  // ignore: missing_return
                },
                // ignore: missing_return
                onRecoverPassword: (data) {},
                // ignore: missing_return
                onSignup: (data) {},
              ),
              Positioned(
                top: 70,
                left: MediaQuery.of(context).size.width / 4.9,
                child: Center(
                  child: Column(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Center(
                          child: TyperAnimatedTextKit(
                              speed: Duration(milliseconds: 300),
//                    totalRepeatCount: 4,
                              isRepeatingAnimation: true,
                              pause: Duration(milliseconds: 1000),
                              text: ["Apartly"],
                              textStyle: GoogleFonts.pacifico(
                                  textStyle: TextStyle(
                                      color: Colors.white,
                                      letterSpacing: 5,
                                      fontSize: 55)),
//                      textStyle: TextStyle(
//                          color: Colors.white,
////                          fontStyle: GoogleFonts.playball(),
//                          fontSize: 55.0,
//                          fontWeight: FontWeight.bold),
//                    pa: Duration(milliseconds: 1000),
                              displayFullTextOnTap: true,
                              stopPauseOnTap: false),
                        ),
                      ]),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
