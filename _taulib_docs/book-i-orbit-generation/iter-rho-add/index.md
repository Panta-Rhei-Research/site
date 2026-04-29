---
{
  "projection_kind": "taulib_declaration",
  "title": "iter_rho_add",
  "permalink": "/verify/taulib/docs/book-i-orbit-generation/iter-rho-add/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Generation`.",
  "declaration_id": "TauLib.BookI.Orbit.Generation::iter_rho_add",
  "declaration_slug": "iter-rho-add",
  "kind": "theorem",
  "name": "iter_rho_add",
  "module_name": "TauLib.BookI.Orbit.Generation",
  "module_url": "/verify/taulib/docs/book-i-orbit-generation/",
  "source_line_start": 70,
  "source_line_end": 75,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L70-L75",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Generation",
        "url": "/verify/taulib/docs/book-i-orbit-generation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L70-L75",
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

- Module: [TauLib.BookI.Orbit.Generation](/verify/taulib/docs/book-i-orbit-generation/)
- Source path: [`TauLib/BookI/Orbit/Generation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L70-L75)
- Source range: L70-L75
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- iter_rho composes: ρⁿ⁺ᵐ(x) = ρⁿ(ρᵐ(x)). -/
```

## Source Excerpt

```lean
theorem iter_rho_add (n m : Nat) (x : TauObj) :
    iter_rho (n + m) x = iter_rho n (iter_rho m x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    simp only [Nat.succ_add, iter_rho_succ, ih]
```
