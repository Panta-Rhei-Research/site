---
{
  "projection_kind": "taulib_declaration",
  "title": "auto_shift",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/auto-shift/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::auto_shift",
  "declaration_slug": "auto-shift",
  "kind": "theorem",
  "name": "auto_shift",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 53,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L53-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L53-L61",
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
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L53-L61)
- Source range: L53-L61
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For non-omega g, φ maps the orbit O_g with constant depth offset. -/
```

## Source Excerpt

```lean
theorem auto_shift (φ : TauAutomorphism) (g : Generator) (hg : g ≠ omega) (n : Nat) :
    φ.toFun ⟨g, n⟩ = ⟨(φ.toFun ⟨g, 0⟩).seed, (φ.toFun ⟨g, 0⟩).depth + n⟩ := by
  induction n with
  | zero => simp
  | succ n ih =>
    have h1 := φ.rho_comm ⟨g, n⟩
    rw [K4_no_jump g hg n, ih] at h1
    rw [K4_no_jump _ (auto_non_omega φ g hg)] at h1
    rw [h1]; congr 1
```
