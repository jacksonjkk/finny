import { Navbar } from "../components/navbar";
import { QuickActions } from "../components/quick-actions";
import { Recents } from "../components/recents";
import { TopLoaners } from "../components/sections/top-loaners";
import { StatusBar } from "../components/status-bar";
export default function Home() {
  return (
    <main className="w-screen h-screen relative">
      <Navbar />
      <section className="w-full h-screen flex flex-col items-center justify-between bg-background">
        <div className="flex flex-col items-center justify-center h-full">
          <QuickActions />
          <Recents />
        </div>
      </section>
      <section className="w-full h-screen flex flex-col items-center justify-between bg-background">
        <TopLoaners />
      </section>
      <StatusBar />
    </main>
  );
}
