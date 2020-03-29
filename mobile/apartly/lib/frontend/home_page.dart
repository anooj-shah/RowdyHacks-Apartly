import 'package:apartly/models/apart_info.dart';
import 'package:convex_bottom_bar/convex_bottom_bar.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';




class MyHome extends StatelessWidget {
  static List<TabItem> tabs = new List<TabItem>();

  @override
  Widget build(BuildContext context) {
    tabs = new List<TabItem>();
    tabs.add(TabItem(title: "Schedule", icon: Icons.access_time));
    tabs.add(TabItem(title: "Explore", icon: Icons.explore));
    tabs.add(TabItem(title: "Profile", icon: Icons.person));

    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => ApartInfo()),
      ],
      child: Container(
        child: Scaffold(
          appBar: AppBar(
            title: Text('Apartly'),

          ),
          bottomNavigationBar: ConvexAppBar(
            onTap: (ind) {
              switch (ind) {
                case 0:
                  Navigator.of(context).canPop()
                      ? Navigator.of(context).popAndPushNamed('/')
                      : print('cant push');
                  break;
                case 1:
                  Navigator.of(context).pushNamed('/ReportPage');
                  break;
                case 2:
                //Navigator.of(context).canPop()
                  Navigator.of(context).pushNamed('/ReportList');
                  // : print('cant push');
                  break;
              }
            },
            items: tabs,
            backgroundColor: Colors.red[600],
            style: TabStyle.fixedCircle,
          ),
//          appBar: AppBar(
//            backgroundColor: Colors.deepOrange,
//          ),
          body: Stack(
            children: <Widget>[
//              MapView(),
//              HomeFAB(),
//              RefreshFAB(),
//              DangerFAB(),
            ],
          ),
        ),
      ),
    );
  }
}
