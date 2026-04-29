---
{
  "projection_kind": "taulib_declaration",
  "title": "sa_i_strong_cp_theorem",
  "permalink": "/verify/taulib/docs/book-iv-particles-strong-cp/sa-i-strong-cp-theorem/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.StrongCP`.",
  "declaration_id": "TauLib.BookIV.Particles.StrongCP::sa_i_strong_cp_theorem",
  "declaration_slug": "sa-i-strong-cp-theorem",
  "kind": "def",
  "name": "sa_i_strong_cp_theorem",
  "module_name": "TauLib.BookIV.Particles.StrongCP",
  "module_url": "/verify/taulib/docs/book-iv-particles-strong-cp/",
  "source_line_start": 49,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L49-L51",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.StrongCP",
        "url": "/verify/taulib/docs/book-iv-particles-strong-cp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L49-L51",
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

- Module: [TauLib.BookIV.Particles.StrongCP](/verify/taulib/docs/book-iv-particles-strong-cp/)
- Source path: [`TauLib/BookIV/Particles/StrongCP.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L49-L51)
- Source range: L49-L51
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The SA-i admissibility condition on C-sector carriers (η-winding preserved
    mod 3) forbids non-trivial topological charge Q_top. An instanton requires
    Δ(η-winding) = +1, which satisfies 1 ≢ 0 (mod 3); an anti-instanton
    requires Δ(η-winding) = −1, satisfying −1 ≢ 0 (mod 3). Both violate SA-i.
    Therefore Q_top = 0 and θ_QCD = 0 exactly.
    Structural origin: K3 (η-winding conservation) + K5 (C-sector χ₋-polarity).
    Scope: established (follows directly from SA-i + instanton topology). -/
```

## Source Excerpt

```lean
def sa_i_strong_cp_theorem : String :=
  "SA-i: Δ(η-winding) ≡ 0 mod 3 → instantons (Δ = ±1) forbidden → " ++
  "Q_top = 0 → θ_QCD = 0 exactly (structural, not dynamical)"
```
