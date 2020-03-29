import 'package:apartly/utilities/constants.dart';
import 'package:auto_size_text/auto_size_text.dart';
import 'package:convex_bottom_bar/convex_bottom_bar.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class ProfilePage extends StatelessWidget {
  static List<TabItem> tabs = new List<TabItem>();

  @override
  Widget build(BuildContext context) {
    tabs = new List<TabItem>();
    tabs.add(TabItem(title: "Schedule", icon: Icons.access_time));
    tabs.add(TabItem(title: "Explore", icon: Icons.explore));
    tabs.add(TabItem(title: "Profile", icon: Icons.person));
    return Container(
      color: Colors.white,
      child: Scaffold(
        appBar: AppBar(
          title: AutoSizeText('Profile',
              style: GoogleFonts.pacifico(
                  textStyle: TextStyle(
                    color: Colors.white,
                    letterSpacing: 5,
                  ))),
        ),
        bottomNavigationBar: ConvexAppBar(
          initialActiveIndex: 2,
          onTap: (ind) {
            switch (ind) {
              case 0:
                Navigator.of(context).canPop()
                    ? Navigator.of(context).pop()
                    : print('cant push');
                break;
              case 1:
                Navigator.of(context).pushNamed('/ExplorePage');
                break;
              case 2:
                //Navigator.of(context).canPop()
                Navigator.of(context).pushNamed('/ReportList');
                // : print('cant push');
                break;
            }
          },
          items: tabs,
          backgroundColor: Constants.themePurple,
          style: TabStyle.reactCircle,
        ),
        body: SafeArea(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.all(18.0),
              child: Container(
                child: Column(children: [
                  CircleAvatar(
                    radius: 100,
                    backgroundImage: ExactAssetImage(
                      "assets/profile.jpg",
                    ),
                  ),
                ]),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
