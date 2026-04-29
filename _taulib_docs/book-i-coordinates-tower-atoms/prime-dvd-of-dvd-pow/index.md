---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_dvd_of_dvd_pow",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/prime-dvd-of-dvd-pow/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::prime_dvd_of_dvd_pow",
  "declaration_slug": "prime-dvd-of-dvd-pow",
  "kind": "theorem",
  "name": "prime_dvd_of_dvd_pow",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 130,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L130-L143",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.TowerAtoms",
        "url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L130-L143",
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

- Module: [TauLib.BookI.Coordinates.TowerAtoms](/verify/taulib/docs/book-i-coordinates-tower-atoms/)
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L130-L143)
- Source range: L130-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Any prime dividing a^e (for e ≥ 1) must divide a. -/
```

## Source Excerpt

```lean
private theorem prime_dvd_of_dvd_pow {p a : TauIdx} (hp : idx_prime p) (e : Nat)
    (he : e ≥ 1) (h : p ∣ a ^ e) : p ∣ a := by
  induction e with
  | zero => omega
  | succ e ih =>
    rw [Nat.pow_succ] at h
    rcases euclid_lemma hp h with h1 | h2
    · -- h1 : p ∣ a ^ e
      rcases e with _ | e
      · -- e = 0: simp gives h1 : p = 1, contradicts p ≥ 2
        simp [Nat.pow_zero] at h1
        exact absurd h1 (by have := hp.1; simp only [TauIdx] at *; omega)
      · exact ih (by omega) h1
    · exact h2
```
