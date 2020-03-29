import 'package:apartly/models/apart_info.dart';
import 'package:apartly/utilities/constants.dart';
import 'package:apartly/widgets/event_card_widget.dart';
import 'package:auto_size_text/auto_size_text.dart';
import 'package:convex_bottom_bar/convex_bottom_bar.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
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
              title: AutoSizeText('Apartly',
                  style: GoogleFonts.pacifico(
                      textStyle: TextStyle(
                    color: Colors.white,
                    letterSpacing: 5,
                  ))),
              actions: <Widget>[
                IconButton(
                  icon: Icon(
                    Icons.search,
                    color: Colors.white,
                  ),
                  onPressed: () {},
                )
              ],
            ),
            bottomNavigationBar: ConvexAppBar(
              initialActiveIndex: 0,

              onTap: (ind) {
                switch (ind) {
                  case 0:
                    Navigator.of(context).canPop()
                        ? Navigator.of(context).popAndPushNamed('/')
                        : print('cant push');
                    break;
                  case 1:
                    Navigator.of(context).pushNamed('/ExplorePage');
                    break;
                  case 2:
                    //Navigator.of(context).canPop()
                    Navigator.of(context).pushNamed('/ProfilePage');
                    // : print('cant push');
                    break;
                }
              },
              items: tabs,
              backgroundColor: Constants.themePurple,
              style: TabStyle.reactCircle,
            ),
//          appBar: AppBar(
//          ),

            body: new ListView.builder(
                itemCount: 100,
//                l: new SliverGridDelegateWithFixedCrossAxisCount(
//                    crossAxisCount: 1),
                itemBuilder: (BuildContext context, int index) {
                  return EventCard();
                })),
      ),
    );
  }
}
