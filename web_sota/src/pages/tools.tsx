import { Settings2, Play, Info } from 'lucide-react';

const TOOLS = [
    { name: 'shopping_manager', description: 'Consolidated tool for shopping lists, offers, and budget tracking.' },
    { name: 'travel_manager', description: 'Travel planning, public transport (Wiener Linien), and weather.' },
    { name: 'expenses_manager', description: 'Programmatic expense tracking and spending analysis.' },
    { name: 'media_manager', description: 'Unified bridge for Plex, Calibre, and Immich libraries.' },
    { name: 'planning_manager', description: 'Personal productivity, todos, and calendar orchestration.' },
];

export function Tools() {
    return (
        <div className="space-y-6">
            <header>
                <h2 className="text-3xl font-bold tracking-tight text-slate-100">Portmanteau Explorer</h2>
                <p className="text-slate-400">Interact with the consolidated toolsets of the Vienna Life Assistant.</p>
            </header>

            <div className="grid gap-6">
                {TOOLS.map((tool) => (
                    <div key={tool.name} className="flex flex-col rounded-xl border border-slate-800 bg-slate-900/50 overflow-hidden backdrop-blur-sm">
                        <div className="flex items-center justify-between bg-slate-800/50 px-6 py-4">
                            <div className="flex items-center gap-3">
                                <Settings2 className="h-5 w-5 text-blue-400" />
                                <span className="font-mono text-sm font-bold text-slate-100 text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">{tool.name}</span>
                            </div>
                            <button className="flex items-center gap-2 rounded-md bg-indigo-600 px-4 py-2 text-xs font-bold text-white hover:bg-indigo-500 transition-colors">
                                <Play className="h-3 w-3" />
                                EXECUTE
                            </button>
                        </div>
                        <div className="p-6">
                            <p className="text-sm text-slate-400 mb-4">{tool.description}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
