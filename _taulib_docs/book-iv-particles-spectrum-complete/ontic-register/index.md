---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_register",
  "permalink": "/verify/taulib/docs/book-iv-particles-spectrum-complete/ontic-register/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.SpectrumComplete`.",
  "declaration_id": "TauLib.BookIV.Particles.SpectrumComplete::ontic_register",
  "declaration_slug": "ontic-register",
  "kind": "def",
  "name": "ontic_register",
  "module_name": "TauLib.BookIV.Particles.SpectrumComplete",
  "module_url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/",
  "source_line_start": 76,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L76-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SpectrumComplete",
        "url": "/verify/taulib/docs/book-iv-particles-spectrum-complete/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L76-L92",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Particles.SpectrumComplete](/verify/taulib/docs/book-iv-particles-spectrum-complete/)
- Source path: [`TauLib/BookIV/Particles/SpectrumComplete.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SpectrumComplete.lean#L76-L92)
- Source range: L76-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete list of fundamental ontic entities constructed in Book IV. -/
```

## Source Excerpt

```lean
def ontic_register : List OnticEntity := [
  ⟨"neutron", .fiberMode, [.C, .A], true⟩,
  ⟨"proton", .fiberMode, [.C, .A, .B], true⟩,
  ⟨"electron", .fiberMode, [.B], true⟩,
  ⟨"photon", .baseMode, [.B], true⟩,
  ⟨"gluon", .fiberMode, [.C], true⟩,
  ⟨"W_boson", .fiberMode, [.A], false⟩,
  ⟨"Z_boson", .fiberMode, [.A, .B], false⟩,
  ⟨"Higgs", .crossingMode, [.Omega], false⟩,
  ⟨"neutrino_e", .baseMode, [.A], true⟩,
  ⟨"neutrino_mu", .baseMode, [.A], true⟩,
  ⟨"neutrino_tau", .baseMode, [.A], true⟩,
  ⟨"up_quark", .fiberMode, [.C, .B], true⟩,
  ⟨"down_quark", .fiberMode, [.C, .B], true⟩,
  ⟨"muon", .fiberMode, [.B], false⟩,
  ⟨"tau_lepton", .fiberMode, [.B], false⟩
]
```
