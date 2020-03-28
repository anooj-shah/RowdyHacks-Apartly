



import 'package:apartly/frontend/home_page.dart';
import 'package:flutter/material.dart';
import 'package:apartly/utilities/constants.dart';



void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: Constants.appName,
      initialRoute: '/',
      routes: {
        // When we navigate to the "/" route, build the MapView Screen
//        '/ReportPage': (context) => ChangeNotifierProvider(
//            create: (context) => FormInfo(), child: ReportPage()),
//        '/ReportList': (context) => new ReportList(),
      },
      theme: ThemeData(
        primaryColor: Colors.red[600],
      ),
      home: MyHome(),
    );
  }
}
