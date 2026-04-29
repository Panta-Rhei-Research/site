---
{
  "projection_kind": "taulib_declaration",
  "title": "auto_omega_to_omega",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/auto-omega-to-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::auto_omega_to_omega",
  "declaration_slug": "auto-omega-to-omega",
  "kind": "theorem",
  "name": "auto_omega_to_omega",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 31,
  "source_line_end": 39,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L31-L39",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Rigidity",
        "url": "/verify/taulib/docs/book-i-orbit-rigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L31-L39",
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

- Module: [TauLib.BookI.Orbit.Rigidity](/verify/taulib/docs/book-i-orbit-rigidity/)
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L31-L39)
- Source range: L31-L39
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Any τ-automorphism maps omega-fiber objects to omega-fiber objects. -/
```

## Source Excerpt

```lean
theorem auto_omega_to_omega (φ : TauAutomorphism) (d : Nat) :
    (φ.toFun ⟨omega, d⟩).seed = omega := by
  have h1 := φ.rho_comm ⟨omega, d⟩
  rw [K2_omega_fixed] at h1
  cases hobj : φ.toFun ⟨omega, d⟩ with | mk s dep =>
  cases s with
  | omega => rfl
  | alpha | pi | gamma | eta =>
    exfalso; rw [hobj] at h1; simp [rho] at h1
```
