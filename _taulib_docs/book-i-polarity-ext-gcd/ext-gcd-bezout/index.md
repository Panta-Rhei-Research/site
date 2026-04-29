---
{
  "projection_kind": "taulib_declaration",
  "title": "ext_gcd_bezout",
  "permalink": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd-bezout/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ExtGCD`.",
  "declaration_id": "TauLib.BookI.Polarity.ExtGCD::ext_gcd_bezout",
  "declaration_slug": "ext-gcd-bezout",
  "kind": "theorem",
  "name": "ext_gcd_bezout",
  "module_name": "TauLib.BookI.Polarity.ExtGCD",
  "module_url": "/verify/taulib/docs/book-i-polarity-ext-gcd/",
  "source_line_start": 56,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L56-L78",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ExtGCD",
        "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L56-L78",
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

- Module: [TauLib.BookI.Polarity.ExtGCD](/verify/taulib/docs/book-i-polarity-ext-gcd/)
- Source path: [`TauLib/BookI/Polarity/ExtGCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L56-L78)
- Source range: L56-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Bézout identity: ↑a * s + ↑b * t = ↑(ext_gcd a b).1. -/
```

## Source Excerpt

```lean
theorem ext_gcd_bezout (a b : Nat) :
    (↑a : Int) * (ext_gcd a b).2.1 + (↑b : Int) * (ext_gcd a b).2.2 =
    ↑(ext_gcd a b).1 := by
  induction b using Nat.strongRecOn generalizing a with
  | _ b ih =>
  unfold ext_gcd
  split
  · -- b = 0: (a, 1, 0). ↑a * 1 + ↑0 * 0 = ↑a ✓
    simp
  · -- b > 0
    rename_i hb
    simp only []
    have hlt : a % b < b := Nat.mod_lt a (by omega)
    have ih' := ih (a % b) hlt b
    -- ih': ↑b * (ext_gcd b (a%b)).2.1 + ↑(a%b) * (ext_gcd b (a%b)).2.2 = ↑(ext_gcd b (a%b)).1
    -- Goal: ↑a * (ext_gcd b (a%b)).2.2 + ↑b * ((ext_gcd b (a%b)).2.1 - ↑(a/b) * (ext_gcd b (a%b)).2.2) = ↑(ext_gcd b (a%b)).1
    set g := (ext_gcd b (a % b)).1
    set x := (ext_gcd b (a % b)).2.1
    set y := (ext_gcd b (a % b)).2.2
    -- Key: a = b * (a/b) + a%b (lifted to Int)
    have hdiv : (↑a : Int) = ↑b * ↑(a / b) + ↑(a % b) := by
      have := Nat.div_add_mod a b; omega
    linear_combination ih' + y * hdiv
```
