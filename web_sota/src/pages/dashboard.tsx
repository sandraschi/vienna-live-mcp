import { Link } from 'react-router-dom';
import { Compass, ShoppingBag, TrainFront, LayoutDashboard, Activity } from 'lucide-react';

export function Dashboard() {
    return (
        <div className="space-y-10 pb-10 relative isolate">
            {/* SOTA Background Aesthetics */}
            <div className="absolute inset-0 -z-10 pointer-events-none overflow-hidden">
                <div className="absolute top-[-5%] left-[-5%] w-[35%] h-[35%] bg-indigo-500/10 blur-[100px] rounded-full" />
                <div className="absolute bottom-[5%] right-[-5%] w-[40%] h-[40%] bg-purple-500/10 blur-[120px] rounded-full" />
            </div>

            {/* Hero Section */}
            <section className="relative overflow-hidden rounded-3xl bg-slate-900/40 border border-slate-800 shadow-2xl backdrop-blur-md">
                <div className="absolute inset-0 bg-gradient-to-br from-indigo-600/20 via-transparent to-purple-600/20" />
                <div className="relative px-8 py-12 md:px-12 md:py-20 max-w-3xl">
                    <div className="inline-flex items-center gap-2 rounded-full bg-indigo-500/10 px-3 py-1 text-xs font-bold text-indigo-400 border border-indigo-500/20 mb-6">
                        <Activity className="h-3 w-3" />
                        VIENNA LIFE ASSISTANT V2
                    </div>
                    <h1 className="text-4xl md:text-6xl font-black tracking-tight text-white mb-6 leading-tight">
                        Your Personal <br /><span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">Vienna Nexus</span>
                    </h1>
                    <p className="text-lg text-slate-400 mb-8 leading-relaxed">
                        The definitive control center for your Viennese life. Programmatic travel planning,
                        automated shopping, and seamless media orchestration through the Portmanteau Pattern.
                    </p>
                    <div className="flex flex-wrap gap-4">
                        <Link to="/tools" className="flex items-center gap-2 rounded-full bg-indigo-600 hover:bg-indigo-500 px-6 py-3 font-bold text-white transition-all transform hover:scale-105 no-underline shadow-lg shadow-indigo-500/20">
                            <Compass className="h-5 w-5" />
                            Start Planning
                        </Link>
                    </div>
                </div>
            </section>

            {/* Quick Access */}
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
                <Link to="/shopping" className="group rounded-2xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm hover:border-indigo-500/50 transition-all no-underline">
                    <ShoppingBag className="h-10 w-10 text-indigo-400 mb-4 group-hover:scale-110 transition-transform" />
                    <h3 className="font-bold text-slate-100">Shopping</h3>
                    <p className="text-sm text-slate-400 leading-tight">Analyze offers at Billa Plus & Hofer.</p>
                </Link>
                <Link to="/travel" className="group rounded-2xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm hover:border-purple-500/50 transition-all no-underline">
                    <TrainFront className="h-10 w-10 text-purple-400 mb-4 group-hover:scale-110 transition-transform" />
                    <h3 className="font-bold text-slate-100">Transit</h3>
                    <p className="text-sm text-slate-400 leading-tight">Next U-Bahn from Alser Straße.</p>
                </Link>
                <Link to="/planning" className="group rounded-2xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm hover:border-blue-500/50 transition-all no-underline">
                    <LayoutDashboard className="h-10 w-10 text-blue-400 mb-4 group-hover:scale-110 transition-transform" />
                    <h3 className="font-bold text-slate-100">Planner</h3>
                    <p className="text-sm text-slate-400 leading-tight">Weekly efficiency report ready.</p>
                </Link>
            </div>
        </div>
    );
}
