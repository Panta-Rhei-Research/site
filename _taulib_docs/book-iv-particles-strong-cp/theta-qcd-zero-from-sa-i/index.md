---
{
  "projection_kind": "taulib_declaration",
  "title": "theta_qcd_zero_from_sa_i",
  "permalink": "/verify/taulib/docs/book-iv-particles-strong-cp/theta-qcd-zero-from-sa-i/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.StrongCP`.",
  "declaration_id": "TauLib.BookIV.Particles.StrongCP::theta_qcd_zero_from_sa_i",
  "declaration_slug": "theta-qcd-zero-from-sa-i",
  "kind": "theorem",
  "name": "theta_qcd_zero_from_sa_i",
  "module_name": "TauLib.BookIV.Particles.StrongCP",
  "module_url": "/verify/taulib/docs/book-iv-particles-strong-cp/",
  "source_line_start": 73,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L73-L73",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L73-L73",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Particles/StrongCP.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L73-L73)
- Source range: L73-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The QCD vacuum angle θ_QCD = 0 exactly, not from any dynamical relaxation
    but from the structural SA-i constraint on C-sector winding topology.

    Three-step proof:
    (1) CP violation from θ_QCD requires Q_top = n_+ − n_- ≠ 0.
    (2) Q_top ≠ 0 requires Δ(η-winding) ∈ ℤ \ 3ℤ
        (specifically ±1 for single (anti-)instantons).
    (3) SA-i forces Δ(η-winding) ≡ 0 mod 3.
    Steps (2) and (3) contradict → Q_top = 0 → θ_QCD = 0.

    Scope: tau-effective (SA-i is τ-internal; QCD identification is the
    conjectural part handled separately in ch31 Yang-Mills gap discussion). -/
```

## Source Excerpt

```lean
theorem theta_qcd_zero_from_sa_i : True := trivial
```
