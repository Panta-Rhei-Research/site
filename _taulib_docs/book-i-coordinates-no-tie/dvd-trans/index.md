---
{
  "projection_kind": "taulib_declaration",
  "title": "dvd_trans'",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-no-tie/dvd-trans/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.NoTie`.",
  "declaration_id": "TauLib.BookI.Coordinates.NoTie::dvd_trans'",
  "declaration_slug": "dvd-trans",
  "kind": "theorem",
  "name": "dvd_trans'",
  "module_name": "TauLib.BookI.Coordinates.NoTie",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-no-tie/",
  "source_line_start": 68,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L68-L70",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.NoTie",
        "url": "/corpus/taulib/docs/book-i-coordinates-no-tie/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L68-L70",
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

- Module: [TauLib.BookI.Coordinates.NoTie](/corpus/taulib/docs/book-i-coordinates-no-tie/)
- Source path: [`TauLib/BookI/Coordinates/NoTie.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/NoTie.lean#L68-L70)
- Source range: L68-L70
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Divisibility is transitive. -/
```

## Source Excerpt

```lean
private theorem dvd_trans' {a b c : Nat} (hab : a ∣ b) (hbc : b ∣ c) : a ∣ c := by
  obtain ⟨k1, hk1⟩ := hab; obtain ⟨k2, hk2⟩ := hbc
  exact ⟨k1 * k2, by rw [hk2, hk1, Nat.mul_assoc]⟩
```
