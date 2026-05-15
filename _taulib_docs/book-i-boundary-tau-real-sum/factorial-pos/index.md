---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.factorial_pos",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/factorial-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealSum`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealSum::TauRat.factorial_pos",
  "declaration_slug": "factorial-pos",
  "kind": "theorem",
  "name": "TauRat.factorial_pos",
  "module_name": "TauLib.BookI.Boundary.TauRealSum",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/",
  "source_line_start": 61,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L61-L66",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealSum",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-real-sum/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L61-L66",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.TauRealSum](/corpus/taulib/docs/book-i-boundary-tau-real-sum/)
- Source path: [`TauLib/BookI/Boundary/TauRealSum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealSum.lean#L61-L66)
- Source range: L61-L66
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `TauRat.factorial n` has positive `toRat` value. -/
```

## Source Excerpt

```lean
theorem TauRat.factorial_pos (n : Nat) : 0 < (TauRat.factorial n).toRat := by
  unfold TauRat.factorial TauRat.toRat TauInt.toInt
  push_cast
  have h : 0 < Nat.factorial n := Nat.factorial_pos n
  have : (0 : Rat) < (Nat.factorial n : Rat) := by exact_mod_cast h
  linarith
```
