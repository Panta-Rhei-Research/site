---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_union_distrib_inter",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/tau-union-distrib-inter/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::tau_union_distrib_inter",
  "declaration_slug": "tau-union-distrib-inter",
  "kind": "theorem",
  "name": "tau_union_distrib_inter",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 300,
  "source_line_end": 325,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L300-L325",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Operations",
        "url": "/verify/taulib/docs/book-i-sets-operations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L300-L325",
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L300-L325)
- Source range: L300-L325
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Dual distributivity: lcm distributes over gcd.
    lcm(a, gcd(b,c)) = gcd(lcm(a,b), lcm(a,c)). -/
```

## Source Excerpt

```lean
theorem tau_union_distrib_inter (a b c : TauIdx) :
    tau_union a (tau_inter b c) = tau_inter (tau_union a b) (tau_union a c) := by
  unfold tau_union tau_inter idx_gcd
  show Nat.lcm a (Nat.gcd b c) = Nat.gcd (Nat.lcm a b) (Nat.lcm a c)
  apply Nat.dvd_antisymm
  · apply Nat.dvd_gcd
    · exact Nat.lcm_dvd (Nat.dvd_lcm_left a b)
        (Nat.dvd_trans (Nat.gcd_dvd_left b c) (Nat.dvd_lcm_right a b))
    · exact Nat.lcm_dvd (Nat.dvd_lcm_left a c)
        (Nat.dvd_trans (Nat.gcd_dvd_right b c) (Nat.dvd_lcm_right a c))
  · have h_dist1 := nat_gcd_distrib_lcm (Nat.lcm a b) a c
    rw [h_dist1]
    have h_abs1 : Nat.gcd (Nat.lcm a b) a = a := by
      rw [Nat.gcd_comm]
      exact Nat.dvd_antisymm (Nat.gcd_dvd_left a _)
        (Nat.dvd_gcd (Nat.dvd_refl a) (Nat.dvd_lcm_left a b))
    rw [h_abs1]
    have h_dist2 : Nat.gcd (Nat.lcm a b) c = Nat.lcm (Nat.gcd c a) (Nat.gcd c b) := by
      rw [Nat.gcd_comm]; exact nat_gcd_distrib_lcm c a b
    rw [h_dist2, ← Nat.lcm_assoc]
    have h_abs2 : Nat.lcm a (Nat.gcd c a) = a := by
      rw [Nat.gcd_comm]
      exact Nat.dvd_antisymm
        (Nat.lcm_dvd (Nat.dvd_refl a) (Nat.gcd_dvd_left a c))
        (Nat.dvd_lcm_left a _)
    rw [h_abs2, Nat.gcd_comm c b]
```
